from django.contrib import admin
from .models import Post, Subject

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        'user_profile',
    )

    ordering = ('created_on',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Subject)