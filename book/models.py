from django.db import models
from django.urls import reverse

class Bk(models.Model):
    title = models.CharField(max_length=200)
    field_name = models.ImageField(upload_to='static/img', height_field=None, width_field=None, max_length=10000)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('bk_detail', args=[self.id])

        
