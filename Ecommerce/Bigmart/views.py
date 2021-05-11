from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import UserDetailsForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from collections import Counter,OrderedDict
# Create your views here.

def Home(request):
    return render(request,'Home.html')

def userregistration(request):
    if request.method=='POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            mobile=request.POST.get('mobile')
            address=request.POST.get('address')
            if password == confirmpassword:
                user = User.objects.create_user(username=name, email=email, password=password)
                UserDetails.objects.create(mobile=mobile,address=address,user=user)
                send_mail('Thank you '+name+' for registration',
                          'Here is your login Below \nhttp://127.0.0.1:9000/Bigmart/login/',
                          settings.EMAIL_HOST_USER,
                          [email]
                          )
                return redirect('/Bigmart/login/')
    form = UserDetailsForm()
    return render(request, 'userregistration.html', {'form': form})

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
           login(request,user)
           return redirect('/Bigmart/productspage/')
        else:
            return render(request, 'userlogin.html',{'comment': 'Enter Valid details'})
    return render(request,'userlogin.html')

def productspage(request):
    products_data=ProductImage.objects.all()
    pi=products_data.values('id','image','product_id__name')
    return render(request, 'productspage.html', {'product_data':pi})

def productdetails(request,id):
    product_image = ProductImage.objects.filter(id=id)
    pd=product_image.values('id','image','product_id','product_id__name','product_id__serialnumber',
                            'product_id__price','product_id__description')
    return render(request,'productdetails.html',{'product_image':pd})

def cartview(request,product_id):# here id is product id
     product_data=Product.objects.get(id=product_id)
     uid = request.user
     id=uid.id
     userdetails=UserDetails.objects.get(user_id=uid.id)
     print(uid)
     if User.is_authenticated:
        Cart.objects.create(user_id=userdetails.user_id,product_id=product_data.id)
     else:
        return redirect('/Bigmart/login/')
     return redirect('cartdet',id)
     # return redirect('/Bigmart/cartdetails/<int:id>/',id=uid.id)

def cartdetails(request,id):# here id is user id
    cd=Cart.objects.filter(user_id=id)
    cv=cd.values_list('product_id',flat=True)
    pd = ProductImage.objects.filter(product_id__in=cv)\
        .values('id','image','product_id','product_id__price',
                'product_id__name','product_id__category_id__name')
    n = cd.values_list('product_id__name', flat=True)
    x = cd.values_list('product_id__price', flat=True)
    count=Counter(n)
    # count=sorted(count.items())

    # cd=Cart.objects.filter(user_id=id)
    # z=cd.values('id','product_id','product_id__price','product_id__name','product_id__category_id__name')
    # x = cd.values_list('product_id__price', flat=True)
    return render(request,'cartdetails.html',{'product_details':pd,'total':sum(x),'count':count})

def deletecartdata(request,product_id):# Here id is product id
    cart_data=Cart.objects.filter(product_id=product_id)
    cart_data.delete()
    id=request.user.id
    return redirect('cartdet',id)

def userlogout(request):
    logout(request)
    return redirect('/Bigmart/login/')