from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from oscar.apps.catalogue.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/catalogue')  # Burada 'home' URL'sini kendi projenizin ana sayfa URL'siyle değiştirmeniz gerekebilir
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/accounts/login')  # Kullanıcı adı ve/veya şifre hatalıysa tekrar giriş yapma sayfasına yönlendirilir
    else:
        return render(request, 'oscar/customer/login_registration.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user, created = User.objects.get_or_create(username=username)
            
            if created:
                user.set_password(password)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('/accounts/login')
            else:
                messages.error(request, 'Username already exists.')
                return redirect('register')
        
        except Exception as e:
            messages.error(request, str(e))
            return redirect('/accounts/login')
    
    return render(request, 'oscar/customer/login_registration.html')




@api_view(['GET'])
def get_product(request):
    try:
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"message": "Ürün bulunamadı."}, status=404)