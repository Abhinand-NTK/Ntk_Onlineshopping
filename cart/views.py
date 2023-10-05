from django.shortcuts import render, redirect, HttpResponse
from admin_auth.models import *
from user_auth.models import *
from .models import Cart
from products import *
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum



def Cart_page(request):
    
    try:
        user = request.session['user']
        user_id = CustomUser.objects.get(email=user)

        request.session['wishlist_count'] = Wishlist.objects.filter(user__email=user).count()
        request.session['cart_count'] = Cart.objects.filter(user__email=user).count()

        if 'user' in request.session:
            cart = Cart.objects.filter(user=user_id)
            total_price = 0  

            for cart_item in cart:
                cart_item.total_price = cart_item.quantity * cart_item.products.price
                total_price += cart_item.total_price

            context = {'cart': cart, 'total_price': total_price}
            return render(request, 'cart_page.html', context)

        return render(request, 'cart_page.html')
    except Exception as e:
        print(e)
        return render(request, 'cart_page.html')

def Add_to_Cart(request, product_vareint_id):

    try:
        if 'user' in request.session:
            user = request.session['user']
            user_id = CustomUser.objects.get(email=user)

         
            if request.method == 'POST':
                quantity = int(request.POST['quantity'])
                product_variant = ProductVariant.objects.get(id=product_vareint_id)

                cart_item_total_quantity = Cart.objects.filter(products=product_variant).aggregate(Sum('quantity'))['quantity__sum'] or 0

                if product_variant.stock < quantity or (cart_item_total_quantity is not None and product_variant.stock < cart_item_total_quantity + quantity):
                    messages.error(request, "The item is out of stock")
                    return redirect('details', id=product_variant.product.id)


                cart_item, created = Cart.objects.get_or_create(
                    user=user_id,
                    products=product_variant,
                    defaults={'quantity': quantity}
                )

                if not created:
                        cart_item.quantity += quantity
                        cart_item.save()
                request.session['wishlist_count'] = Wishlist.objects.filter(user__email=user).count()
                request.session['cart_count'] = Cart.objects.filter(user__email=user).count()

                return redirect('cart_item')
            # request.session['wishlist_count'] = Wishlist.objects.filter(user__email=user).count()
            # request.session['cart_count'] = Cart.objects.filter(user__email=user).count()

    except Exception as e:
        print(e)
        return redirect('cart_item')

  
def Cart_delete(request, delete_id):
    try:
        if 'user' in request.session:
            delete = Cart.objects.get(id=delete_id)

            delete.delete()
            return redirect('cart_item')
    except Exception as e:
        print(e)
        return redirect('cart_item')




def Checkout(request):
    try:
        if 'user' in request.session:

            user = request.session['user']
            user_id = CustomUser.objects.get(email=user)

            cart = Cart.objects.filter(user=user_id)
            total_price = 0  
            discount_price = 0  
            tax = 0  
            GrandTotal = 0

            for cart_item in cart:
                cart_item.total_price = cart_item.quantity * cart_item.products.price
                total_price += cart_item.total_price

            request.session['redirected'] = False

            if request.method == 'POST':
                coupencode = request.POST.get('coupencode').strip()

                request.session['coupencode'] = coupencode


                current_datetime = timezone.now()

                try:
                    coupon = Coupons.objects.get(
                        coupon_code=coupencode, valid_from__lte=current_datetime, valid_to__gte=current_datetime)
                except Coupons.DoesNotExist:
                    coupon = None  
                    messages.error(
                        request, "The coupon does not exist or is not valid")
                    return redirect('check_out')

                if coupon and coupon.active:
                    if coupon.discount_amount > 0 and total_price >= coupon.minimum_order_amount:
                        discount_price = coupon.discount_amount
                        messages.success(request, 'Applied Sucessfully')
                    elif coupon.discount > 0 and total_price >= coupon.minimum_order_amount:
                        if total_price < coupon.maximum_order_amount_the_discount_percenetage_applicable_for:
                            discount_price = (total_price * coupon.discount) / 100
                        else:
                            discount_price = (
                                coupon.maximum_order_amount_the_discount_percenetage_applicable_for * coupon.discount) / 100
                    else:
                        messages.error(
                            request, f"Applicable only for :- {coupon.minimum_order_amount}")

                else:
                    messages.error(request, "The coupen  is not valid")
            if total_price > 0 and total_price < 1000:
                tax = (total_price*5)/100
            elif total_price > 0 and total_price > 1000:
                tax = (total_price*12)/100
            GrandTotal = total_price-discount_price+tax
            address_user = UserAdress.objects.filter(user=user_id)

            if GrandTotal <= 0:
                # Check if not already redirected
                if not request.session.get('redirected', False):
                    request.session['redirected'] = True  # Set the flag
                    messages.error(
                        request, "There is nothing in the cart to proceed!!!!!")
                    return redirect('cart_item')
            else:
                pass

            coupen = Coupons.objects.all()

            context = {
                'address_user': address_user,
                'total_price': total_price,
                'cart': cart,
                'discount_price': discount_price,
                'tax': tax,
                'GrandTotal': GrandTotal,
                'coupen': coupen
            }
            return render(request, 'checkout.html', context)
        else:
           
            return redirect('login')
    except Exception as e:
        print(e)
        return redirect('login')




def update_cart_item_quantity(request):

 

    # try:


        if request.method == 'POST':
            item_id = request.POST.get('id')
            action = request.POST.get('action')
            var_id = request.POST.get('var_id')
            cart_item = Cart.objects.get(id=item_id)

            check_quantity = ProductVariant.objects.get(id=var_id)
            cart_Stock = check_quantity.stock

            if action == 'incr':
                cart_item.quantity += 1
            elif action == 'decr' and cart_item.quantity > 0:
                cart_item.quantity -= 1

            if check_quantity.stock < cart_item.quantity or cart_item.quantity == 0:
                pass
            elif check_quantity.stock == cart_item.quantity:
                cart_item.save()
            else:
                cart_item.save()


            message = "none"


            user = request.session.get('user')
            wishlist_count = Wishlist.objects.filter(user__email=user).count()
            cart_count = Cart.objects.filter(user__email=user).count()
            request.session['wishlist_count'] = request.session['wishlist_count']+ wishlist_count
            request.session['cart_count'] = request.session['cart_count'] + cart_count

           


            total_price = cart_item.products.price * cart_item.quantity

            response_data = {'new_quantity': cart_item.quantity,
                            'new_total_price': total_price,
                            'message': message,
                            'cart_Stock': cart_Stock,
                            'cart_count':cart_count,}
            return JsonResponse(response_data)
    # except Exception as e:
    #     print(e)
    #     return JsonResponse(response_data)


