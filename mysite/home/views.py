
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from home.forms import ProfileUpdateForm, SearchForm, SignUpForm, UserUpdateForm
from product.models import Category, Coment, Images, Product, ShopCart, ShopCartForm

from home.models import ContactForm, ContactFormMessage, Settings, UserProfileInfo
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    newproduct = Product.objects.all()[:10]
    setting = Settings.objects.all()
    category = Category.objects.all()
    dayproduct = Product.objects.all()[:4]
    lastproduct = Product.objects.all().order_by('-id')[:4]
    pickproduct = Product.objects.all().order_by('?')[:4]
    
    
    context = {'setting':setting,
                'page':'home',
                'newproduct':newproduct,
                'category':category,
                'dayproduct':dayproduct,
                'lastproduct':lastproduct,
                'pickproduct':pickproduct,
                
                }

    return render(request,'index.html',context)
def category_detail(request,id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    image = Images.objects.filter(product_id=id)
    comments = Coment.objects.filter(product_id=id,status='True')

    context = {
        'category':category,
        'product':product,
        'image':image,
        'comments':comments
    }



    return render(request,'category_detail.html',context)
def aboutus(request):
    category = Category.objects.all()
    setting1 = Settings.objects.get(pk=1)
    context1 = {'setting1':setting1,'category':category}
    return render(request,'aboutus.html',context1)
def references(request):
    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    context = {'setting':setting,'category':category}
    return render(request,'references.html',context)
def contact(request):

    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.message=form.cleaned_data['message']
            data.subject=form.cleaned_data['subject']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Comment was sent sucessfuly')
            return HttpResponseRedirect('/contact')


    form = ContactForm()
    category = Category.objects.all()
    setting = Settings.objects.get(pk=1)
    context = {'setting':setting,'form':form,'category':category }
    return render(request,'contact.html',context)
def products(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)



    context = {'products':products,'category':category,'categorydata':categorydata}

    
    return render(request, 'products.html', context)
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            
            products = Product.objects.filter(tittle__icontains=query)
           
            context = {
                'products':products,
                'category':category,
            }
            return render(request,'search.html',context)
    return HttpResponseRedirect('/')        


import json


def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    product = Product.objects.filter(tittle__icontains=q)
    results = []
    for pl in product:
      product_json = {}
      product_json = pl.tittle 
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request,user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
            
        else:
            # Return an 'invalid login' error message.
            messages.warning(request,'Username or Password is invalid')
            return HttpResponseRedirect('/login')

    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'login.html',context)


def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            django_login(request,user)
            current_user=request.user
            data=UserProfileInfo()
            data.user_id=current_user.id
            data.image="images/users/users.png"
            data.save()
            return HttpResponseRedirect('/')
    form=SignUpForm()
    category = Category.objects.all()
    context={
        'category':category,
        'form':form
    }
    return render(request,'signup.html',context)

def user_profile(request):
    current_user=request.user
    category = Category.objects.all()
    userprofile=UserProfileInfo.objects.get(user_id=current_user.id)
    context = {
        'userprofile':userprofile,
        'category':category,
    }
    return render(request,'user_profile.html',context)
def edit(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your info has been changed')
            return redirect('/user_profile')
    else:
        category=Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        
        context = {
        
                'category':category,
                'user_form':user_form,
                'profile_form':profile_form,
    }
    return render(request,'edit.html',context)
