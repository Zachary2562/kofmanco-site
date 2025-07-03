from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_published')
    list_filter = ('is_published', 'created_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
