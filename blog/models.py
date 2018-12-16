from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=2048)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)