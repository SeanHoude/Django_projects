from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
