from django.contrib import admin
from .models import Post, Author, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "text",)
    fields = ("author", "category", "title", "text", "slug", "published_date", )
    # list_filter = ('finish',)
    # ordering = ('-finish',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
