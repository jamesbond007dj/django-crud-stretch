from django.db import models
from django.urls import reverse

class Store(models.Model):


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('mov_detail', args=[self.id])
