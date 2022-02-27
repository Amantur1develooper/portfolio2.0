from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    if request.method =='POST':
        customer=Name()
        customer.name=request.POST.get('name')
        customer.email=request.POST.get('email')
        customer.work1=request.POST.get('site')
        customer.work2=request.POST.get('telegram_bot')
        customer.work3=request.POST.get('backend')
        customer.work4=request.POST.get('frontend')
        customer.work5=request.POST.get('seo')
        customer.work6=request.POST.get('talk')
         
        customer.description=request.POST.get('site')
        customer.description=request.POST.get('telegram_bot')
        # customer.email=request.POST.get('c_email')
        # customer.address=request.POST.get('c_address')
        customer.save()
    myprojects=Myworks.objects.all()
    return render(request,"index.html",{'projects':myprojects})