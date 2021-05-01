from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class FeaturedTuberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_featured = True)



class Youtuber(models.Model):

    crew_choices = (        
        ('solo','solo'),
        ('medium','medium'),
        ('large','large'),
    )

    camera_choices = (
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('red','red'),
        ('panasonic','panasonic'),
        ('fuji','fuji'),
        ('other','other'),
    )

    category_choices = (
        ('code','code'),
        ("mobile_review","mobile_review"),
        ("gaming","gaming"),
        ("vlogs","vlogs"),
        ("cooking","cooking"),
        ("film_making","film_making"),
        ("comedy","comedy"),
    )


    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="media/ytuber/%Y/%m")
    video_url = models.CharField(max_length=150)
    description = RichTextField()
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    age = models.IntegerField()
    height = models.IntegerField()
    camera_type = models.CharField( choices = camera_choices ,max_length=150)
    subs_count = models.IntegerField()
    category = models.CharField( choices = category_choices ,max_length=250)
    is_featured = models.BooleanField(default = False)
    crew = models.CharField( choices =crew_choices ,max_length=150)
    created_date = models.DateTimeField(default = datetime.now, blank =True)

    # defining managers
    objects = models.Manager()
    featured_tubers = FeaturedTuberManager()
    
