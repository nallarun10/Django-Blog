from django.contrib import admin
from blogging.models import Post, Category

class BookInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [BookInline,]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline,]
    exclude = ('post',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)