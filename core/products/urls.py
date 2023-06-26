from django.urls import path
from . import views
from .views import login_view, register_view

urlpatterns = [
    path('denemeget/', views.get_product),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),
]