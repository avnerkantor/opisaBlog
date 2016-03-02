from django.contrib import admin
from .models import Post, Author, Category, Tag

''' POST ADMIN '''


def make_published(self, request, queryset):
    queryset.update(status='p')


make_published.short_description = 'Publish Post yang ditandai'


def make_draft(self, request, queryset):
    queryset.update(status='d')


make_draft.short_description = 'Draft Post yang ditandai'


def make_archive(self, request, queryset):
    queryset.update(status='a')


make_archive.short_description = 'Archive Post yang ditandai'


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "status")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "text",)
    fields = ("author", "category", "title", "text", "slug", "published_date", 'status')
    # list_filter = ('finish',)
    # ordering = ('-finish',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
