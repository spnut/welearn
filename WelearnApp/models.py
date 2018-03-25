from django.db import models

# Create your models here.
class Item(models.Model):
    post_text = models.TextField(default='')
    comment = models.TextField(default='')
    detail = models.TextField(default='')
    def __str__(self):
        return self.comment
