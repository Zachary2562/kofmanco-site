from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('products/pricepilot/', views.pricepilot_detail, name='pricepilot_detail'),
] 