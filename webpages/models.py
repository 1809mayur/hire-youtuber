from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/slider/%Y")       # %Y,%m added to create an another folder the basis of year or month.
    your_link = models.URLField(max_length=200,blank =True)
    def __str__(self):               # used to change the slider object with any field from the class slider.
        return self.headline      

class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=100)
    insta_link = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)
    youtube_link = models.URLField(max_length=200,blank = True)

    def __str__(self):
        return self.first_name
    

