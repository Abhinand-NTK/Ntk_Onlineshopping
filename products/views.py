import json
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from admin_auth.models import *
from user_auth.models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core import serializers
from user_auth.forms import RatingForm
from order.models import *
from cart.models import *
from django.db.models import Avg

# Create your views here.


def home(request):

    try:

        user = request.session.get('user')

        products = Product.objects.all().order_by('-id')[:8]
        productsvarient = ProductVariant.objects.all()
        brand = Brand.objects.all().order_by('id')
        banner = Banner.objects.all().order_by('id')

        mens = Product.objects.filter(men=True)
        count1 = mens.count()
        request.session.save()

        Womans = Product.objects.filter(woman=True)
        count2 = Womans.count()
        request.session.save()

        kids = Product.objects.filter(kids=True)
        count3 = kids.count()
        request.session.save()

        combos = Product.objects.filter(combos=True)
        count4 = combos.count()
        request.session.save()

        request.session['wishlist_count'] = Wishlist.objects.filter(
            user__email=user).count()
        request.session['cart_count'] = Cart.objects.filter(
            user__email=user).count()
        
        average_ratings_list = []

        for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)
                
        print(average_ratings_list)
        print(average_ratings_list)
        print(average_ratings_list)
                
        data=zip(products,average_ratings_list)


        context = {'count1': count1, 'count2': count2, 'count3': count3, 'count4': count4, 'products': products,
                   'brand': brand, 'banner': banner,'data':data }

        return render(request, "home.html", context)
    except Exception as e:
        print(e)
        return render(request, "home.html", context)


def product_category(request):

    try:

        sizes = Size.objects.all().order_by('id')
        color = Color.objects.all().order_by('id')

        context = {'sizes': sizes, 'color': color}

        return render(request, 'category_management_userside.html', context)
    except Exception as e:
        print(e)
        return render(request, 'category_management_userside.html', context)


def Womans(request, id=None):

    try:

        items_per_page = 6

        if id:
            id_sub = Subcategory.objects.get(name=id)
            products = Product.objects.filter(
                Q(woman=True), subcategory=id_sub).order_by('id')
            min_prices_per_product = []

            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = []  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.append(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

        elif id == None:
            products = Product.objects.filter(
                Q(woman=True))

            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = set()
                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    product_sizes.add(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

        elif request.method == 'POST':
            pass

        products_for_filter = Product.objects.filter(
            Q(woman=True))
        heading = "Woman"
        cat = set()
        for product in products_for_filter:
            subcategory = product.subcategory
            cat.add(subcategory)

        per_page = 6

        paginator = Paginator(products, per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        average_ratings_list = []

        for product in products:
            average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                Avg('rating_user'))['rating_user__avg']
            average_ratings_list.append(
                int(average_rating) if average_rating is not None else None)

        zipped_data = zip(page, min_prices_per_product, average_ratings_list)

        size = Size.objects.all()
        color = Color.objects.all()

        context = {'page': page, 'products': products, 'cat': cat, 'heading': heading, 'min_prices_per_product':
                   min_prices_per_product, 'zipped_data': zipped_data, 'sizes': sizes, 'size': size, 'color': color, }

        return render(request, "category_management_userside.html", context)
    except Exception as e:
        print(e)
        return render(request, "category_management_userside.html", context)


def Mens(request, id=None):

    try:

        if id:

            id_sub = Subcategory.objects.get(name=id)

            products = Product.objects.filter(
                Q(men=True) or Q(kids=True), subcategory=id_sub).order_by('id')
            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = []

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    product_sizes.append(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

            print(average_ratings_list)

        else:

            products = Product.objects.filter(
                Q(men=True) or Q(kids=True)).order_by('id')
            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = set()  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.add(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

                average_ratings_list = []

                for product in products:
                    average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                        Avg('rating_user'))['rating_user__avg']
                    average_ratings_list.append(
                        int(average_rating) if average_rating is not None else None)

        print(average_ratings_list)

        products_for_filter = Product.objects.filter(
            Q(men=True) or Q(kids=True)).order_by('id')

        heading = "Men"

        cat = set()
        for product in products_for_filter:
            subcategory = product.subcategory
            cat.add(subcategory)

        per_page = 6  # You can change this to your desired number

        paginator = Paginator(products, per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        average_ratings_list = []

        for product in products:
            average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                Avg('rating_user'))['rating_user__avg']
            average_ratings_list.append(
                int(average_rating) if average_rating is not None else None)

        print(average_ratings_list)

        zipped_data = zip(page, min_prices_per_product, average_ratings_list)

        size = Size.objects.all().order_by('id')
        color = Color.objects.all().order_by('id')

        context = {'page': page, 'products': products, 'cat': cat, 'heading': heading, 'min_prices_per_product':
                   min_prices_per_product, 'zipped_data': zipped_data, 'sizes': sizes, 'size': size, 'color': color}
        return render(request, "category_management_userside.html", context)
    except Exception as e:
        print(e)
        return render(request, "category_management_userside.html", context)


def kids(request, id=None):
    try:
        if id:
            id_sub = Subcategory.objects.get(name=id)

            products = Product.objects.filter(
                Q(kids=True), subcategory=id_sub).order_by('id')

            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = []  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.append(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

        else:
            products = Product.objects.filter(
                Q(kids=True)).order_by('id')
            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = set()  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.add(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

        products_filter = Product.objects.filter(
            Q(kids=True)).order_by('id')

        heading = "Kids"
        cat = set()
        for product in products_filter:
            subcategory = product.subcategory
            cat.add(subcategory)

        per_page = 6  # You can change this to your desired number

        paginator = Paginator(products, per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        average_ratings_list = []

        for product in products:
            average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                Avg('rating_user'))['rating_user__avg']
            average_ratings_list.append(
                int(average_rating) if average_rating is not None else None)

        zipped_data = zip(page, min_prices_per_product, average_ratings_list)

        size = Size.objects.all().order_by('id')
        color = Color.objects.all().order_by('id')

        context = {'page': page, 'products': products, 'cat': cat, 'heading': heading, 'min_prices_per_product':
                   min_prices_per_product, 'zipped_data': zipped_data, 'sizes': sizes, 'size': size, 'color': color}
        return render(request, "category_management_userside.html", context)
    except Exception as e:
        print(e)
        return render(request, "category_management_userside.html", context)


def combos(request, id=None):
    try:

        if id:
            id_sub = Subcategory.objects.get(name=id)

            products = Product.objects.filter(
                Q(combos=True), subcategory=id_sub)

            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = set()  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.add(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)
        else:
            products = Product.objects.filter(
                Q(combos=True))

            min_prices_per_product = []
            sizes = {}

            for product in products:
                product_variants = ProductVariant.objects.filter(
                    product=product)

                min_price = None
                product_sizes = set()  # Create a list to store sizes for the current product

                for variant in product_variants:
                    price = variant.price
                    size = variant.size

                    if min_price is None or price < min_price:
                        min_price = price

                    # Add size to the product_sizes list
                    product_sizes.add(size)

                min_prices_per_product.append(min_price)
                sizes[product.name] = product_sizes

            average_ratings_list = []

            for product in products:
                average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)

        products_filter = Product.objects.filter(
            Q(combos=True))
        heading = "Combos"
        cat = set()
        for product in products_filter:
            # Assuming 'subcategory' is a field in your Product model
            subcategory = product.subcategory
            cat.add(subcategory)

        per_page = 6  # You can change this to your desired number

        paginator = Paginator(products, per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        average_ratings_list = []

        for product in products:
            average_rating = Rating.objects.filter(product_variant__product=product).aggregate(
                Avg('rating_user'))['rating_user__avg']
            average_ratings_list.append(
                int(average_rating) if average_rating is not None else None)

        zipped_data = zip(page, min_prices_per_product, average_ratings_list)

        size = Size.objects.all().order_by('id')
        color = Color.objects.all().order_by('id')

        context = {'page': page, 'size': size, 'color': color, 'products': products, 'cat': cat, 'heading': heading,
                   'min_prices_per_product': min_prices_per_product, 'zipped_data': zipped_data, 'sizes': sizes}
        return render(request, "category_management_userside.html", context)
    except Exception as e:
        print(e)
        return render(request, "category_management_userside.html", context)


def product_details(request, id=None):

    try:

        user = request.session.get('user')
        user_id = None

        if user:
            user_id = CustomUser.objects.get(email=user)

        request.session['wishlist_count'] = Wishlist.objects.filter(
            user__email=user).count()
        request.session['cart_count'] = Cart.objects.filter(
            user__email=user).count()

        ordercheck = OrderProduct.objects.filter(
            variant__product__id=id, customer=user_id)

        order_list_id = []
        for item in ordercheck:
            order_list_id.append(item.variant.id)

        wishlist = Wishlist.objects.all()
        varinet_data = ProductVariant.objects.all()

        product = get_object_or_404(Product, id=id)
        product_variants = ProductVariant.objects.filter(product=product)

        for i in product_variants:
            print(i.id)

        serialized_product_variants = serializers.serialize(
            'json', product_variants)
        request.session['product_variants_json'] = serialized_product_variants

        product_variant_images = {}

        for variant in product_variants:
            variant_images = Multipleimges.objects.filter(product=variant)
            first_image = variant_images.first()

            if first_image:
                product_variant_images[variant.id] = (
                    first_image.images.url, variant.color)

        product_vareint_data = []

        print(product_variants)

        for var in product_variants:
            print(var.id)
            varient_data = {
                'id': var.id,
                'color': var.color,
                'price': var.price,
                'size': var.size,
                'stock': var.stock,
            }
            product_vareint_data.append(varient_data)

        color = Color.objects.get(name='Black')

        rating_form = RatingForm()

        product_variants1 = ProductVariant.objects.filter(
            product=product, color=color)

        images = Multipleimges.objects.filter(product__in=product_variants)
        testing = Multipleimges.objects.filter(product__in=product_variants1)
        rating = Rating.objects.filter(user=user_id)
        ratingall = Rating.objects.filter(product_variant__product__id=id)
        ratingcount = ratingall.count()

        rating_varient_id = []

        for i in rating:
            rating_varient_id.append(i.product_variant.id)

        size = Size.objects.all()
        color = Color.objects.all()

        context = {'wishlist': wishlist,
                   'varinet_data': varinet_data,
                   'size': size, 'color': color,
                   'product': product,
                   'product_variants': product_variants,
                   'images': images,
                   'product_vareint_data': product_vareint_data,
                   'product_variant_images': product_variant_images,
                   'rating_form': rating_form,
                   'rating': rating_varient_id,
                   'ratingall': ratingall,
                   'ordercheck': ordercheck,
                   'order_list_id': order_list_id,
                   'ratingcount': ratingcount,
                   }

        return render(request, 'products_detalils.html', context)
    except Exception as e:
        print(e)
        return render(request, 'products_detalils.html', context)


def Filtering_in_Prouduct_details_page(request):

    try:

        if request.method == 'POST':

            data = json.loads(request.body.decode('utf-8'))

            color = data.get('color')
            variant_id = data.get('variant_id')

            varient = ProductVariant.objects.get(id=variant_id)

            varient_color = str(varient.color)
            varient_size = str(varient.size)
            varient_price = str(varient.price)
            varient_stock = str(varient.stock)
            varient_id = str(variant_id)

            testing = Multipleimges.objects.filter(product=varient)

            image_urls = [img.images.url for img in testing]

            response = {'varient_id': varient_id, 'varient_stock': varient_stock, 'varient_price': varient_price,
                        'varient_size': varient_size, 'varient_color': varient_color, 'image_urls': image_urls}

            return JsonResponse(response)
    except Exception as e:
        print(e)


def Filter(requset, category_id=None, heading=None):

    try:

        current_route = requset.path

        segments = current_route.strip('/').split('/')
        last_segment = segments[-1] if segments else None

        if last_segment == 'Men':
            return Mens(requset, category_id)
        elif last_segment == 'Woman':
            return Womans(requset, category_id)
        elif last_segment == 'Kids':
            return kids(requset, category_id)
        elif last_segment == 'Combos':
            return combos(requset, category_id)
    except Exception as e:
        print(e)
        return combos(requset, category_id)


def filter_Accordence_multiple_input(request, heading=None):

    response_data = {}

    try:
        current_route = request.path

        segments = current_route.strip('/').split('/')

        last_segment = segments[-1] if segments else None

        if request.method == 'POST':

            selected_colors = request.POST.getlist('colorCheckbox')
            selected_sizes = request.POST.getlist('sizeCheckbox')

            min_range_value = request.POST.get('myRangeMin', None)
            max_range_value = request.POST.get('myRangeMax', None)

            name = request.POST.get('name_search', None)

            if min_range_value == 0:
                min_range_value = None

            if max_range_value == 0:
                max_range_value = None

            if last_segment == 'Men':

                products_in = Product.objects.filter(
                    Q(men=True))
                heading = "Men"

            if last_segment == 'Woman':

                products_in = Product.objects.filter(
                    Q(woman=True))
                heading = "Woman"

            if last_segment == 'Kids':

                products_in = Product.objects.filter(
                    Q(kids=True) or Q(men=True))
                heading = "Kids"

            if last_segment == 'Combos':

                products_in = Product.objects.filter(
                    Q(combos=True))
                heading = "Combos"

            products = ProductVariant.objects.filter(product__in=products_in)

            if min_range_value is not None and max_range_value is not None:

                products = products.filter(
                    Q(price__gte=min_range_value) & Q(price__lte=max_range_value))

            if selected_colors:
                products = products.filter(color__in=selected_colors)

            if selected_sizes:
                products = products.filter(size__in=selected_sizes)

            if name:

                if heading == "Men":

                    product = Product.objects.filter(
                        name__icontains=name, men=True, woman=False, kids=False, combos=False)

                    products = ProductVariant.objects.filter(product__in=product)

                if heading == "Woman":

                    product = Product.objects.filter(
                        name__icontains=name, men=False, woman=True, kids=False, combos=False)

                    products = ProductVariant.objects.filter(product__in=product)

                if heading == "Kids":

                    product = Product.objects.filter(
                        name__icontains=name, men=False, woman=False, kids=True, combos=False)

                if heading == "Combos":

                    product = Product.objects.filter(
                        name__icontains=name, men=False, woman=False, kids=False, combos=True)

                    products = ProductVariant.objects.filter(product__in=product)

            average_ratings_list = []
            nums = []
            i = 0

            for product in products:
                average_rating = Rating.objects.filter(product_variant=product).aggregate(
                    Avg('rating_user'))['rating_user__avg']
                average_ratings_list.append(
                    int(average_rating) if average_rating is not None else None)
                nums.append(i)
                i = i+1

            print(average_ratings_list)
            print(average_ratings_list)
            print(average_ratings_list)

            product_data = set()

            product_data = (
                {
                    'id': product.product.id,
                    'name': product.product.name,
                    'color': product.color.name,
                    'size': product.size.name,
                    'price': product.price,
                    'image': product.product.images.url,
                    'average_ratings_list': average_ratings_list,
                    'nums': nums,

                    # Add more fields as needed
                }
                for product in products
            )

            if products:
                n = True
            else:
                n = False

            data = zip(average_ratings_list,product_data)

            size = Size.objects.all()
            color = Color.objects.all()

            response_data = {
                'message': 'Success',
                'products': product_data,
                'size': size,
                'color': color,
                'heading': heading,
                'n': n,
                'data':data,
            }
        return render(request, 'multiplefilterproducts.html', response_data)

    except Exception as e:
        print(e)
        return render(request, 'multiplefilterproducts.html', response_data)


@require_GET
def search_products(request, query):

    try:

        query1 = query

        if query:
            products = Product.objects.filter(name__icontains=query1)[
                :10]

            suggestions = [{'name': product.name} for product in products]
        else:
            suggestions = []
        return JsonResponse(suggestions, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(suggestions, safe=False)
