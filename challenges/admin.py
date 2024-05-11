from django.contrib import admin
from .models import Challenge, GalleryImage
from .forms import GalleryImageForm


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    form = GalleryImageForm
    extra = 3  


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]  


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass  