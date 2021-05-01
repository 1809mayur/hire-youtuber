from django.db import models
from datetime import datetime
# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254,blank=True) 
    user_id = models.IntegerField(blank =True)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    created_date = models.DateTimeField(default = datetime.now,blank =True)
    message= models.TextField()

    # def __str__(self):
    #     return self.email
    