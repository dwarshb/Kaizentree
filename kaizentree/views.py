from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Item,Category,Tag
from django.contrib.auth.decorators import login_required
from .serializers import ItemSerializer, CategorySerializer, TagSerializer
from rest_framework import generics
from django.http import JsonResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.create_user(username=username, email=username, password=password)
            
        if user is not None:
            login(request, user)
            messages.success(request, 'Account Created successful.')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signup.html')

@login_required
def dashboard(request):
    items = Item.objects.all()
    category_count = Category.objects.count()
    item_count = Item.objects.count()
    return render(request, 'dashboard.html', {'items': items,'category_count': category_count, 'item_count': item_count})
    
class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    def post(self, request, *args, **kwargs):
        # Handle POST request to create a new category
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=201)

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def post(self, request, *args, **kwargs):
        # Handle POST request to create a new category
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=201)

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def post(self, request, *args, **kwargs):
        # Handle POST request to create a new category
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=201)
