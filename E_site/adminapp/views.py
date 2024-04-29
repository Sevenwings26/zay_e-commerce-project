# Create your views here.
from django.shortcuts import render, redirect

# modules for form creation 
from . forms import signupForm, loginForm, Product_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import productTable
from django.contrib.auth.models import User 


# modules for login decorators
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.decorators import permission_required


# # Method 1 - Sign up creation 
# # Create views with the forms 
# def signup(request):
    
#     form = signupForm()
    
#     if request.method == "POST":
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['first_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password'] 
        
#         if password == confirm_password:
#             new_user = User.objects.create_user(
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#             )
#             new_user.set_password(password)
#             new_user.save()
#             messages.success(request, "Account created successfully. Please Login!")
#             return redirect('login')
        
#     return render(request, "registration/signup.html", {"form":form})


# # Method 2 - Sign up creation 
# # sign up from the userCreationForm 
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            
            # authentication and login
            usermane = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            user = authenticate(username=usermane, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
        
    else:
        form = signupForm()
    return render(request, 'registration/signup.html', {'form': form})
    
    
    
def log_in(request):
    form = loginForm()
    if request.method == "POST":
        users = request.POST
        username = users['username']
        password = users['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('login')
        
    return render(request, "registration/login.html", {"form":form})


def log_out(request):
    logout(request)
    return redirect('home')

def reset_password(request):
    return render(request, 'registration/resetpassword.html')




"""PRODUCT VIEW"""
@login_required
def product_upload(request):
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()        
            messages.success(request, "You have successfully uploaded product(s)")
            return redirect('product_upload')
    else:
        form = Product_form()
        return render(request, 'adminupload.html', {'form': form})


@login_required
def product_table(request):
    products = productTable.objects.all()
    return render(request, 'products-view.html', {'products': products})

# delete record
@login_required
def delete_product(request, productId):
    if request.user.is_autheticated():        
        delete_it = productTable.objects.get(productId=productId)
        delete_it.delete()
        messages.success(request, "Record successfully deleted.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete a record...")
        return redirect('home')
    
# modify product 
def modify_product(request, productId):
    modify = productTable.objects.get(productId=productId)
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES, instance=modify)
        if form.is_valid():
            form.save()
            messages.success(request, "Product modified successfully")
            return redirect('products')
    else:
        form = Product_form(instance=modify)
        context = {'form': form}
    return render(request, 'modify_product.html', context)
    


# Users view 
def users_view(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'index-users.html', {'users': users})
    else:
        return redirect('home')


def user_individual(request):
    return render(request, 'users.html')



def index_page(request):
    products = productTable.objects.all()
    return render(request, 'index.html', {'products': products})

