from django.db import models

# Create your models here.
class Links(models.Model):
    email = models.EmailField(max_length=254)
    fb_link = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    insta_link = models.CharField(max_length=150)
    yt_link = models.CharField(max_length=150)
    mobile = models.CharField(max_length=10,blank = True)
    country_code = models.CharField(max_length=50,blank =True)
   