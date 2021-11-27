from django.shortcuts import redirect, render

from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from product.models import CommentForm,Coment, ShopCart, ShopCartForm

# Create your views here.
def index1(request):
    return HttpResponse("hello product")
@login_required(login_url='/login') # login check
def addcomment(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data=Coment()
            data.user_id=current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Your comment was sent succesfuly')
            url=request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
            #return HttpResponse("Saved")
    return HttpResponse("Register don't completed")
@login_required(login_url='/login') # login check
def AddToCart(request,id):
    url=request.META.get('HTTP-REFERER')
    if request.method == 'POST':
        form=ShopCartForm(request.POST)
        if form.is_valid():
            current_user=request.user
            data = ShopCart()
            data.user_id=current_user.id
            data.product_id=id
            data.quantity=form.cleaned_data['quantity']
            data.save()
            return HttpResponseRedirect(url)
