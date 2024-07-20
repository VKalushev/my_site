from django.contrib import admin
from .models import Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {'slug': ("title",)}
    list_filter = ("date","title","author")
    list_display = ("title", "author","date")

class AuthorAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("first_name","last_name")
    list_display = ("first_name", "last_name")

class TagAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("caption",)
    list_display = ("caption",)

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)