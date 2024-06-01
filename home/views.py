from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from .forms import Table1Form
from .models import Customer, Ordertable, Producttable1, Orderdetails
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db import IntegrityError





import json


def register(request):
    if request.method == 'POST':
        form = Table1Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('/login/')
    else:
        form = Table1Form()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':        #user has submitted the login-form
        username = request.POST.get('name')
        password = request.POST.get('password')
        users = Customer.objects.all()
        for user in users:
            if user.name == username and check_password(password, user.password):
                request.session['username'] = user.name
                return redirect('/homepage/')
        error_message = "Invalid username or password." 
        return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')


#add to cart function:
def add_to_cart(request):           #just a function to add items to cart
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = Producttable1.objects.get(productid=product_id)
        
        # Ensure cart is a list
        cart = request.session.get('cart', [])   #it checks the previous session cart value and 0 if no cart was there
        if not isinstance(cart, list):
            cart = []
        
        cart.append({'product_id': product_id, 'quantity': quantity, 'product_name': product.productname, 'product_price': product.prdouctprice})
        request.session['cart'] = cart
       
        return redirect('view_cart')
    else:
        return redirect('homepage')


#view cart function:
def view_cart(request):         #method to show the cart items and then confirm/clear acc to user choice
    cart = request.session.get('cart', [])
    cart_items = [{'product': Producttable1.objects.get(productid=item['product_id']), 'quantity': item['quantity']} for item in cart]
    return render(request, 'view_cart.html', {'cart_items': cart_items})



def confirm_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        user_name = request.session.get('username')
        user = Customer.objects.get(name=user_name)  
        current_datetime = timezone.now()
        
        # Calculate total price of the order
        total_price = sum(item['quantity'] * item['product_price'] for item in cart)
        
        try:
            # Create the order with the total price
            order = Ordertable.objects.create(user=user, order_date=current_datetime, totalprice=total_price)
            
            for item in cart:
                product = Producttable1.objects.get(productid=item['product_id'])
                quantity = item['quantity']
                Orderdetails.objects.create(order=order, product=product, quantity=quantity)
            
            # Clear the cart
            del request.session['cart']
            return redirect('homepage')
        except IntegrityError:
            messages.error(request, 'Error: There was a problem confirming your order. Please try again later.')
            return redirect('view_cart')
    else:
        return redirect('view_cart')



# clearing the cart
def clear_cart(request):
    if request.method == 'POST':
        if 'cart' in request.session:
            del request.session['cart']
    return redirect('view_cart')  # Redirect back to the view cart page after clearing the cart


# homepage view
def homepage(request):
    products = Producttable1.objects.all()
    username = request.session.get('username')
    return render(request, 'homepage.html', {'products': products, 'username': username})


#logOut
def logout_view(request):
    request.session.flush()
    return redirect('/login/')

#about
def about_view(request):
    return render(request,'about.html')


#Contact
def contact_view(request):
    return render(request,'contactus.html')


#landing page
def landing(request):
    return render(request, 'landingpage.html')

#review page
def review_view(request):
    return render(request, 'reviews.html')


#importing food items from json file to Product model table 
def import_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            product = Producttable1(
                productid=item['id'],
                productname=item['name'],
                prdouctprice=item['price'],
                productdesc=item['desc'],
                image_path=item['image']
                
            )
            product.save()

json_file_path = 'templates/items.json'
import_data_from_json(json_file_path)

