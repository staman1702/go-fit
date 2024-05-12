from django.db import models
from django.utils.text import slugify
from community.models import Subject

STATUS = ((0, "Active"), (1, "Archived"))

# Create your models here.
   
class Challenge(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subjects = models.ManyToManyField(Subject, blank=True)   
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ["start_date"]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class GalleryImage(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='challenge_gallery/')