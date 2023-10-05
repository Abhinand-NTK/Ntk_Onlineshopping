from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from admin_auth.models import CustomUser
from user_auth.models import UserAdress
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from random import randint
from order.models import *
from collections import defaultdict
from cart.models import *
from user_auth.forms import *
import json
import random
import string
from datetime import datetime
import re



def User_login(request):
    try:
        if 'admin' in  request.session:
                return redirect('admindashboard')

        if request.method=='POST':
            password=request.POST['password']
            email=request.POST['username']

            
        
            hashed_password = make_password(password, hasher='pbkdf2_sha256')

            user = authenticate(email=email, password=password)
            check=CustomUser.objects.filter(email=email)
        


            if user:
                    if  user.is_blocked:
                        print("Its coming here !!!")
                        messages.error(request,"Your Acccount is blocked")
                        User_logout(request)

                    elif user.is_verified and user.is_authenticated and not user.is_blocked:
                        userlogin(request, user)  # Log the user in
                        request.session['user'] = email
                        # if user in request.session:
                        
                        return redirect('home')
                        
                    else:
                        return redirect('otp_verification', user_id=user.id)
            
            else:
                messages.error(request, "Check the email or password")
                # return redirect('user_login')


        return render(request,'Authenticatoins/loginpage.html')
    except Exception as e:
        print(e)
        return render(request,'Authenticatoins/loginpage.html')



def userlogin(request,user):

    login(request,user)


def User_logout(request):
    logout(request)
    if 'user' in request.session:
        del request.session['user']
    return redirect('user_login')



def Signupvalidation(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)
        print(data.get('useremail'))

        print(CustomUser.objects.filter(email = data.get('useremail')))

        if CustomUser.objects.filter(email = data.get('useremail')):
             response = {'message':'The email id is alredy exist !!'}
             return JsonResponse(response)
        else:
            response = {'message':'Enter Your E-mail !!'}
            return JsonResponse(response)
        
def Addpropic(request,user_id):
  
    if request.method == 'POST':
        profilepic= request.FILES.get('profilepicture', None)
        print(profilepic)
        print(profilepic)
        print(profilepic)
        print(profilepic)
        print(profilepic)
        user=CustomUser.objects.get(id=user_id)
        user.images = profilepic
        user.save() 
        return redirect('myprofile')
    
def generate_referral_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def User_signup(request):
        
    # try:
        if request.method=='POST':
            email=request.POST['username']
            password=request.POST['password']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            repeatpassword=request.POST['repeatpassword']
            referral_code = request.POST['referral_code']

            check=CustomUser.objects.filter(email=email)

            if referral_code:
                try:
                    referrer = CustomUser.objects.get(referral_code=referral_code)
                    referrer.wallet = referrer.wallet + 100
                    referrer.save()
                    wallerhistory_referer=Payementwallet(user=referrer)
                    wallerhistory_referer.paymenttype="Credit"
                    wallerhistory_referer.created=datetime.now()
                    wallerhistory_referer.save()
                
                   
                except CustomUser.DoesNotExist:
                    referrer = None
            else:
                referrer = None



            
            if check:
                messages.error(request,'The E-mail is Already exist Try with another one')
                return redirect('user_signup')
            if password==repeatpassword:
            
                
                otp = generate_and_send_otp()  # Generate OTP here
                user=CustomUser.objects.create_user(email,password=password,)
                user.first_name = firstname
                user.lastname = lastname
                # user.phone_number = phonenumber
                user.otp=otp
                user.referral_code=generate_referral_code()
                user.referrer=referrer
                user.save()
                user_id=user.id

                payhis =  CustomUser.objects.get(email = email)
                payhis.referrer 

                if payhis.referrer :
                        
                        payhis.wallet = payhis.wallet + 100
                        payhis.save()


                        wallerhistory=Payementwallet(user=payhis)
                        wallerhistory.paymenttype="Credit"
                        wallerhistory.created=datetime.now()
                        wallerhistory.save()
                


                subject = "Email Confirmation OTP"
                message = f"Your OTP for email confirmation is: {otp}"
                from_email = "testntk123@gmail.com"  # Replace with your email
                recipient_list = [email]  # 'email' is the recipient's email address

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                
                return redirect('otp_verification',user_id)
            else:
                messages.error(request,'Password fiels are Not matchining  !')
                return redirect('user_signup')

        return render(request, 'Authenticatoins/signup.html')
    # except Exception as e:
    #     print(e)
    #     return render(request, 'Authenticatoins/signup.html')



def generate_and_send_otp():
    try:
        otp = randint(100000, 999999)
        return otp
    except Exception as e:
        print(e)
        return otp


def User_otpverification(request,user_id):
    try:

        user = CustomUser.objects.get(id=user_id)
        context = {'user': user}
        print(user.otp)

        if request.method == 'POST':
            verification = request.POST['otp']
            print(verification)

            if verification==user.otp:
                user.otp = ''
                user.is_verified = True
                user.wallet = user.wallet + 100
                user.save()  # Save the user after updating is_email_verified

                wallerhistory=Payementwallet(user=user)
                wallerhistory.paymenttype="Credit"
                wallerhistory.created=datetime.now()
                wallerhistory.save()
                
                messages.success(request, 'Email verification is successful')
                return redirect('user_login')  # Use return to perform the redirect
            else:
                messages.error(request, 'Please enter a valid OTP')

        return render(request, 'Authenticatoins/verification.html', context)
    except Exception as e:
        print(e)
        return render(request, 'Authenticatoins/verification.html', context)



def User_forgetpassword(request):
    try:
        if request.method == 'POST':
            reset_email = request.POST['resetpassword']
            try:
                user = CustomUser.objects.get(email=reset_email)
                return redirect('reset_password', user_id=user.id)
            except CustomUser.DoesNotExist:
                messages.error(request, 'User with this email does not exist')
        return render(request, 'Authenticatoins/forgotpassword.html')
    except Exception as e:
        print(e)
        return render(request, 'Authenticatoins/forgotpassword.html')


def User_resetpassword(request, user_id):
    try:
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('user_login')
        
        if request.method == 'POST':
            password = request.POST['resetpassword']
            repeat_password = request.POST['password']
            if password == repeat_password:
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successful')
                return redirect('user_login')
            else:
                messages.error(request, 'Passwords do not match')
        
        return render(request, 'Authenticatoins/resetpassword.html', {'user': user})
    except Exception as e:
        print(e)
        return render(request, 'Authenticatoins/resetpassword.html', {'user': user})
        

    
def Manage_Address(request):
    try:
        current_path = request.path
        if 'user' in request.session:
            user=request.user
        
        else:
            messages.error(request,'Sesson time Out')
            return redirect('user_login')
            
        if request.method=='POST':
                print("Abhinand")
                
                first_name=request.POST['firstname']
                last_name=request.POST['lastname']
                phonenumber=request.POST['phonenumber'].strip()
                address=request.POST['address']
                town=request.POST['town']
                zip_code=request.POST['zipcode'].strip()
                nearbylocation=request.POST['nearbylocation']
                district=request.POST['district']

                # phonenumber = request.form.get("phonenumber").strip()
                # zipcode = request.form.get("zipcode").strip()

                pattern = r'^\d{10}$'

                if re.match(pattern, phonenumber):
                    pass
                else:
                    messages.error(request,'The phonenumber field should be digits')
                    return redirect('manageadress')
            
                zipcode = r'^\d{6}$'

                if re.match(zipcode, zip_code):
                    pass
                else:
                    messages.error(request,'The Pin field should be  6 digits')
                    return redirect('manageadress')


                address=UserAdress(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    phonenumber=phonenumber,
                    address=address,
                    town=town,
                    zip_code=zip_code,
                    nearbylocation=nearbylocation,
                    district=district
                    )
                address.save()

                if '/cart/check_out' in request.META['HTTP_REFERER']:
                    return redirect('check_out')
                elif '/manageadress' in request.META['HTTP_REFERER']:
                    return redirect('manageadress')
        address_user=UserAdress.objects.filter(user=user)
        context={
            'address_user':address_user
        }

    
        return render(request,'manageadress.html',context) 
    except Exception as e:
        print(e)
        return render(request,'manageadress.html',context) 


def Manage_Edit_Address(request, adress_id):
    try:
        if 'user' in request.session:
            user = request.user
        else:
            messages.error(request, 'Session time Out')
            return redirect('user_login')
            
        try:
            address = UserAdress.objects.get(id=adress_id, user=user)
        except UserAdress.DoesNotExist:
            messages.error(request, 'Address not found')
            return redirect('manageadress')
        
        if request.method == 'POST':
            # Get the form data
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            phonenumber = request.POST['phonenumber']
            address_text = request.POST['address']
            town = request.POST['town']
            zip_code = request.POST['zipcode']
            nearby_location = request.POST['nearbylocation']
            district = request.POST['district']

          

            pattern = r'^\d{10}$'

            if re.match(pattern, phonenumber):
                    pass
            else:
                    messages.error(request,'The phonenumber field should be digits')
                    return redirect('manageadress')
            
            zipcode = r'^\d{6}$'

            if re.match(zipcode, zip_code):
                    pass
            else:
                    messages.error(request,'The Pin field should be  6 digits')
                    return redirect('manageadress')

            # Update the address fields
            address.first_name = first_name
            address.last_name = last_name
            address.phonenumber = phonenumber
            address.address = address_text
            address.town = town
            address.zip_code = zip_code
            address.nearbylocation = nearby_location
            address.district = district

            # Save the changes
            address.save()
            if '/cart/check_out' in request.META['HTTP_REFERER']:
                    return redirect('check_out')
            elif '/manageadress' in request.META['HTTP_REFERER']:
                    return redirect('manageadress')

            # return redirect('manageadress')

        context = {
            'address_user': [address],  # Pass the address as a list to the template
        }

        return render(request, 'manageadress.html', context)
    except Exception as e:
        print(e)
        return render(request, 'manageadress.html', context)

def Manage_Address_delete(request,adress_id):
    try:
        if 'user' in request.session:
            user=request.user
            
        
        else:
            messages.error(request,'Session time Out')
            return redirect('user_login')
        address=UserAdress.objects.get(id=adress_id)
        address.delete()
        if '/cart/check_out' in request.META['HTTP_REFERER']:
                    return redirect('check_out')
        elif '/manageadress' in request.META['HTTP_REFERER']:
                    return redirect('manageadress')
    except Exception as e:
        print(e)
        return redirect('manageadress')



def Myprofile(request):
    try:
        if 'user' in request.session:
            if request.method=='POST':
                return render(request, 'manageadress.html')

            
        personal_details = CustomUser.objects.all()
        context = {'personal_details': personal_details}
            
        return render(request, 'myprofile.html', context)
    except Exception as e:
        print(e)
        return render(request, 'myprofile.html', context)




    
def Edit_profile(request):
    try:
         if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            profilepic = request.FILES['profilepicture']
            user_email = request.user  
            user = CustomUser.objects.get(email=user_email)  
            
            if user.check_password(password):  
                user.first_name = firstname
                user.lastname = lastname  
                user.images = profilepic
                user.save()                  
                messages.success(request, "Profile updated successfully")
                return redirect('myprofile')
            else:
                messages.error(request, "Incorrect password")
                return redirect('myprofile')
            
         return render(request,'myprofile.html')
    except Exception as e:
        print(e)
        return render(request,'myprofile.html')

def Myorder(request):

    try:
        user = request.user
        orders = OrderProduct.objects.filter(customer=user).order_by('id')
        
        order_dict = defaultdict(list)

        for order in orders:
            order_dict[order.order_id].append(order)

        context = {
            'order': orders,
            'order_dict': dict(order_dict),  
        }

        return render(request, 'myorder.html', context)
    except Exception as e:
        print(e)
        return render(request, 'myorder.html', context)


def Coupenlist(requset):
    try:
        coupens=Coupons.objects.all().order_by('id')
        context={
            'coupens':coupens
            }
        return render(requset,'coupenlistuserside.html',context)
    except Exception as e:
        print(e)
        return render(requset,'coupenlistuserside.html',context)


def Mywallet(request):

    try:
     
        user = request.session['user']
        user_id = CustomUser.objects.get(email=user)
        waller_history=Payementwallet.objects.filter(user__email=user)

        return render(request,'mywallet.html',{'waller_history': waller_history})
    except Exception as e:
        print(e)
        return render(request,'mywallet.html',{'waller_history': waller_history})


def Mywishlist(request, varient_id=None):
    try:
        user = request.session['user']
        user_id = CustomUser.objects.get(email=user)
        
        request.session['wishlist_count'] = Wishlist.objects.filter(user__email=user).count()
        request.session['cart_count'] = Cart.objects.filter(user__email=user).count()

        wishlist=Wishlist.objects.filter(user=user_id)

        if varient_id: 
            product_variant_instance = get_object_or_404(ProductVariant, id=varient_id)

            try:
                wishlist_exist_or_not = Wishlist.objects.get(product=product_variant_instance)
                wishlist_exist_or_not.delete()
                return JsonResponse({'message': 'The item is removed from the Wishlist'})
            except Wishlist.DoesNotExist:
                wishlist = Wishlist(user=user_id,product=product_variant_instance)
                wishlist.check_color=True
                wishlist.save()
                check=Wishlist.objects.get(product=product_variant_instance)
                check_Color=check.check_color
                print(check_Color)
                return JsonResponse({'message': 'The item is added to the Wishlist','check':check_Color})
            
        return render(request, 'wishlist.html',{'wishlist':wishlist})
    except Exception as e:
        print(e)
        return render(request, 'wishlist.html',{'wishlist':wishlist})
        

def Delete_wish(requset,delete_id):
    Wishlis=Wishlist.objects.get(id=delete_id)
    Wishlis.delete()
    return JsonResponse("Success")

def Add_item_to_Cart(request,product_vareint_id=None):

    try:
        
        user = request.session['user']

        request.session['wishlist_count'] = Wishlist.objects.filter(user__email=user).count()
        request.session['cart_count'] = Cart.objects.filter(user__email=user).count()

        user_id = CustomUser.objects.get(email=user)

        check_wish=Wishlist.objects.get(id=product_vareint_id)

        varient=ProductVariant.objects.get(id=check_wish.product.id)



        check_is_the_item_in_Cart_or_not=Cart.objects.filter(user=user_id, products=varient)

        if check_is_the_item_in_Cart_or_not:
            messages.info(request,"The item is already in the cart")
            return redirect('mywishlist', varient_id = 0)
        elif varient.stock <=0:
            messages.info(request,"The item is Out of stock")
            return redirect('mywishlist', varient_id = 0)

    

        
        else:

            if request.method == 'POST':
                    quantity = int(request.POST['quantity'])

                    cart_item, created = Cart.objects.get_or_create(
                        user=user_id,
                        products=varient,
                        defaults={'quantity': quantity}
                    )

                    if not created:
                        cart_item.quantity += quantity
                        cart_item.save()
                    return redirect('cart_item')
    except Exception as e:
        print(e)
        return redirect('cart_item')





def Submit_rating(request, variant_id):  
    try:
        user = request.session.get('user')  

        if request.method == 'POST':
            try:
                data = json.loads(request.body.decode('utf-8'))

                rating = data.get('rating')
                review_comment = data.get('review_comment')

                print(rating)
                print(review_comment)

                check_submission_status = Rating.objects.filter(
                    user=CustomUser.objects.get(email=user),
                    product_variant=ProductVariant.objects.get(id=variant_id) 
                )

                if not check_submission_status:  
                    print("succeeded")
                    print("succeeded")

                    rating_form = RatingForm(data={'rating_user': rating, 'review_comment': review_comment})

                    if rating_form.is_valid():
                        rating = rating_form.save(commit=False)
                        rating.user = request.user 
                        rating.product_variant = ProductVariant.objects.get(id=variant_id) 
                        rating.save()

            except json.JSONDecodeError:
                return JsonResponse({'message': 'Invalid JSON data'}, status=400)

        return JsonResponse({'message': 'Rating submitted successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Rating submitted successfully'})

def Print_invoice(request,order_id):
    
    order=Order.objects.filter(order_id=order_id).order_by('id')
    order_product=OrderProduct.objects.filter(order_id__order_id=order_id)
    eachproduct_quantity_price = []
    for item in order_product:
        eachproduct_quantity_price.append(item.quandity * item.variant.price)

    zipdata = zip(order_product, eachproduct_quantity_price)


    return render(request,'invoice.html',{'zipdata':zipdata,'order':order,'order_product':order_product,'eachproduct_quantity_price':eachproduct_quantity_price,})

