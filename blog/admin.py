from django.contrib import admin

from .models import Post, Comment, Category
# Register your models here.

class CommentsInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class CustomPostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']

    list_display= ['title', 'slug','author', 'created_at']

    list_filter = ['title', 'slug']

    prepopulated_fields = {'slug': ['title']}

    inlines = [CommentsInline]

class CustomCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, CustomPostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CustomCategoryAdmin)