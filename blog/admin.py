from django.contrib import admin
from .models import Author,Post,Tag,Comment
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name","email_id"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["caption"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","date","slug","author"]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment)