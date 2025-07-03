from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib import messages
from .forms import ContactForm

def home(request):
    """Homepage view"""
    return render(request, 'main/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f'Contact form submitted: {name}, {email}, {message}')
            messages.success(request, 'Thank you for your message!')
            return redirect('main:contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def products(request):
    return render(request, 'main/products.html')

def pricepilot_detail(request):
    return render(request, 'main/pricepilot_detail.html')
