from django.db import models

# Create your models here.

class Topic(models.Model):
    post_text = models.TextField(default='')
    detail = models.TextField(default='')    
    '''def __str__(self):
        return self.comment'''

class Comment(models.Model):
    cm = models.TextField(default='')
    comment = models.ForeignKey(Topic,default=None, on_delete=models.CASCADE)
