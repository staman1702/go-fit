from django.db import models
from django.utils.text import slugify
from profiles.models import UserProfile

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Subject(models.Model):

    class Meta:
        verbose_name_plural = 'Subjects'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_DEFAULT,
                                     default=1, related_name="posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    subjects = models.ManyToManyField('Subject', blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | posted by {self.user_profile}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)