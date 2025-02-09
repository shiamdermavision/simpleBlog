from django.db import models

#cetagory
class Category(models.Model):
     name = models.CharField(max_length=255)
     description = models.CharField(max_length=300)

#artical

class Article(models.Model):
     categories = models.ManyToManyField(Category, blank=True, null=True, on_delete=models.SET_NULL)
     name = models.CharField(max_length=500)
     description = models.TextField
