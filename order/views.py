from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from admin_auth.models import *
from user_auth.models import *
from .models import *
import datetime
from cart.models import *
from collections import defaultdict
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from user_auth.models import UserAdress 
import json
from django.http import JsonResponse

# Create your views here.

def Place_Order(request):

    try:
        if 'user' in request.session:
            user = request.session['user']
            userid = CustomUser.objects.get(email=user)

            if request.method == 'POST':
            
                data = json.loads(request.body)
                address_id = data.get('address',None)
                total = data.get('total',None)
                order_total = float(data.get('order_total'))
                payement_method = data.get('payment_method',None)
                discount = data.get('discount_price',None) 
                tax = data.get('tax',None)

                coupencode = request.session.get('coupencode', None)
            
                if order_total<=0:
                    messages.error(request,"Choose Your products to Continue!!")
                    return redirect('check_out')

                address = UserAdress.objects.get(id=address_id)

                if not address:
                    messages.error(request, 'Choose an Address to proceed')
                    

                order = Order()
                order.user = userid
                order.address = address
                order.total = total
                order.discount = discount
                order.order_total = order_total
                order.tax = tax
                order.paid_amount = order_total
                order.save()

                payment = Payments()
                payment.user = userid
                payment.payement_method = payement_method
                payment.total_amount = order_total
                payment.save()

                if payement_method == "cod":
                    payment.status = 'Pending'
                    payment.save()
                    order.payment_method="Cod"
                    order.save()


                elif payement_method == "op":
                    payment.status=="Credited"
                    payment.payement_method="Op"
                    payment.is_paid=True
                    payment.save()
                
                elif payement_method == "wallet":
                    payment.status=="Credited"
                    payment.is_paid=True
                    payment.save()
                    order.payment_method="Wallet"
                    order.save()

                    
                    wallerhistory=Payementwallet(user=userid)
                    wallerhistory.paymenttype="Credit"
                    wallerhistory.save()

                    walletmoney=CustomUser.objects.get(email=user)
                    walletmoney.wallet = float(walletmoney.wallet )- order_total
                    walletmoney.save() 



                yr = int(datetime.date.today().strftime('%Y'))
                dt = int(datetime.date.today().strftime('%d'))
                mt = int(datetime.date.today().strftime('%m'))
                d = datetime.date(yr, mt, dt)
                current_date = d.strftime("%Y%m%d")
                order_id = current_date + str(order.id)
                order.order_id = order_id
                order.save()

                if payement_method == "cod":
                    payment.payment_id = order_id + "COD"
                    payment.save()
                elif payement_method == "op":
                    payment.payment_id = order_id + "OP"
                    payment.status = "paid"
                    payment.save()
                    
                elif payement_method == "wallet":
                    payment.payment_id = order_id + "Wallet"
                    payment.status = "paid"
                    payment.save()
                    
                    

                if coupencode:
                    coupon = Coupons.objects.get(coupon_code=coupencode)
                    order.coupon = coupon
                    order.save()

                cart_items = Cart.objects.filter(user=userid)
                for item in cart_items:
                    variant = ProductVariant.objects.get(id=item.products.id)
                    order_item = OrderProduct.objects.create(
                        order_id=order,
                        customer=userid,
                        variant=variant,
                        quandity=item.quantity,
                        product_price=item.products.price,
                        ordered="True",
                        payment=payment,

                    )
                    order.payement = payment
                    variant.stock = variant.stock - item.quantity
                    variant.save()
                    order.is_ordered=True
                    order.save()
                    item.delete()

                if payement_method=="cod":
                    pass    
                    
                if payement_method=="op":
                    response_d={'order_id': order_id}
                    return JsonResponse(response_d)
                    
                response_data = {'message': 'Data received successfully','order_id': order_id}
                return JsonResponse(response_data)

        return JsonResponse(response_data)
    except Exception as e:
        print(e)
        return JsonResponse(response_data)


def Place_Order_online_Payment(request):

    try:

   
        if 'user' in request.session:
            user = request.session['user']
            userid = CustomUser.objects.get(email=user)

            if request.method == 'POST':


                
                coupencode = request.session.get('coupencode', None)
                address_id = request.POST['address']
                total = request.POST['total_price']
                order_total = float(request.POST['GrandTotal'])
                discount = request.POST['discount_price']
                tax = request.POST['tax']
                payement_method = request.POST['payment-method']


                if order_total<=0:
                    messages.error(request,"Choose Your products to Continue!!")
                    return redirect('check_out')

                address = UserAdress.objects.get(id=address_id)

                if not address:
                    messages.error(request, 'Choose an Address to proceed')
                    

                order = Order()
                order.user = userid
                order.address = address
                order.total = total
                order.discount = discount
                order.order_total = order_total
                order.tax = tax
                order.paid_amount = order_total
                order.save()

                payment = Payments()
                payment.user = userid
                payment.payement_method = payement_method
                payment.total_amount = order_total
                payment.save()

                


                if payement_method == "op":
                    payment.status=="Credited"
                    payment.is_paid=True
                    payment.save()
                    order.payment_method="Op"
                    order.save()



                yr = int(datetime.date.today().strftime('%Y'))
                dt = int(datetime.date.today().strftime('%d'))
                mt = int(datetime.date.today().strftime('%m'))
                d = datetime.date(yr, mt, dt)
                current_date = d.strftime("%Y%m%d")
                order_id = current_date + str(order.id)
                order.order_id = order_id
                order.save()

            
                if payement_method == "op":
                    payment.payment_id = order_id + "OP"
                    payment.save()
                    

                if coupencode:
                    coupon = Coupons.objects.get(coupon_code=coupencode)
                    order.coupon = coupon
                    order.save()

                cart_items = Cart.objects.filter(user=userid)
                for item in cart_items:
                    variant = ProductVariant.objects.get(id=item.products.id)
                    order_item = OrderProduct.objects.create(
                        order_id=order,
                        customer=userid,
                        variant=variant,
                        quandity=item.quantity,
                        product_price=item.products.price,
                        ordered="True",
                        payment=payment,

                    )
                    order.payement = payment
                    variant.stock = variant.stock - item.quantity
                    variant.save()
                    # order.status=''
                    order.is_ordered=True
                    order.save()
                    item.delete()

                if payement_method=="op":
                    response_d={'order_id': order_id}
                    return JsonResponse(response_d)
        return JsonResponse(response_d)
    except Exception as e:
        print(e)
        return JsonResponse(response_d)


            





def remove_show_modal_session(request):
    if 'show_modal' in request.session:
        del request.session['show_modal']

    return redirect('myorder')


def Order_deatails(request, order_id):
    try:
        if 'user' in request.session:

            details = Order.objects.get(order_id=order_id)

            user = request.user
            orders = OrderProduct.objects.filter(order_id=details)

            if orders.exists():
                first_order_has_return_request = orders.first().return_request
            else:
                first_order_has_return_request = False


            context = {
                'orders': orders,

                'details': details,

                'first_order_has_return_request': first_order_has_return_request,
            }

            return render(request, 'orderdetails.html', context)
    except Exception as e:
        print(e)
        return render(request, 'orderdetails.html', context)


        
def Returntheorder(request,order_id):
    try:
        if request.method=='POST':
            ordernote=request.POST['return_reason']

            order=Order.objects.get(id=order_id)
            order.ordernote=ordernote
            order.status="Return requested"
            order.save()
            return redirect('order_details',order.order_id)
    except Exception as e:
        print(e)
        return redirect('order_details',order.order_id)

def Cancelorder(request,order_id):
    try:
        if request.method=='POST':
            cancelnote=request.POST['cancel_reason']
            order=Order.objects.get(id=order_id)
            order.cancelnote=cancelnote
            order.status="Cancelled"
            order.save()

            if order.payment_method == 'Op':

                user_wallet=CustomUser.objects.get(id=order.user.id)
                user_wallet.wallet=user_wallet.wallet + int(order.paid_amount)
                user_wallet.save()

                wallerhistory=Payementwallet(user=order.user)
                wallerhistory.paymenttype="Credit"
                wallerhistory.save()
                
            return redirect('order_details',order.order_id)
    except Exception as e:
        print(e)
        return redirect('order_details',order.order_id)

        
    
def Cancel_indivdal_items(request,id):
    try:
        if request.method=='POST':
            return_Reason=request.POST['return_single_reason']
            product=OrderProduct.objects.get(id=id)
            product.return_request='True'
            product.return_reason=return_Reason
        

            product.save() 
            return redirect('order_details',product.order_id)
    except Exception as e:
        print(e)
        return redirect('order_details',product.order_id)





def get_address_details(request):
    try:
        if  request.method == 'GET':
            
            address_id = request.GET.get('id')
            address = get_object_or_404(UserAdress, id=address_id)

            address_details = {
                'first_name': address.first_name,
                'last_name': address.last_name,
                'phonenumber': address.phonenumber,
                'address': address.address,
                'town': address.town,
                'zip_code': address.zip_code,
                'nearbylocation': address.nearbylocation,
                'district': address.district,
                'created': address.created,
            }

            return JsonResponse(address_details, content_type="application/json")

        return JsonResponse({'error': 'Invalid request'})
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Invalid request'})




def razorpaycheck(request):
    try:
        if request.method == 'POST':
            total_price = request.POST.get('total_price')
            discount_price = request.POST.get('discount_price')
            tax = request.POST.get('tax')
            GrandTotal = request.POST.get('GrandTotal')
            payment_method = request.POST.get('payment-method')

            response_data = {
                'message': 'Form data received successfully',
                'total_price': total_price,
                'discount_price': discount_price,
                'tax': tax,
                'GrandTotal': GrandTotal,
                'payment_method': payment_method,
            }

            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Invalid request method'}, status=400)


        

def Refunded_for_indivdal_items(request,itemid):
        try:
         
            product=OrderProduct.objects.get(id=itemid)
            order=Order.objects.get(order_id=product.order_id)
            order_amount=order.order_total
            amount_of_the_product=product.variant.price * product.quandity
            user_wallet=CustomUser.objects.get(id=order.user.id)
            user_wallet.wallet=user_wallet.wallet+amount_of_the_product
            user_wallet.save()

            wallerhistory=Payementwallet(user=order.user)
            wallerhistory.paymenttype="Credit"
            wallerhistory.save()
        
            product.return_accept='True'

            product.save() 
            refunded=True  

            return JsonResponse({'refunded':refunded}) 
        except Exception as e:
            print(e)
            return JsonResponse({'refunded':refunded}) 












