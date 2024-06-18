from django.contrib.auth.models import User
from datetime import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now) # baraie zakhire va entedhare tarikh post estefade mikonnand .
    created=models.DateTimeField(auto_now_add=True) # vaghti post zakhire mishavand tarikham be soorate khodkar zakhire mishavand .
    updated=models.DateTimeField(auto_now=True)    #vaghti zakhire mikone tarikh be soorate khodkar zakhire mishavand .
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

# -publish : be tartibe noozooli post haro montasher mikonnand :
    class Meta:
        ordering = ['-publish'] 
        # ?????  
        indexes = [
            models.Index(fields=['-publish']),
            ]   

    # vasse inke be soorate namayesh ya yek reshte dar biyayand :
    def __str__(self):
        return "Blog Title: "+self.title


