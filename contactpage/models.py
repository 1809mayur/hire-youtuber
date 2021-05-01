from django.db import models
from datetime import datetime


# Create your models here.
class ReachUs(models.Model):
    full_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    company_name = models.CharField(max_length=250,blank=True)
    subject = models.CharField(max_length=250)
    details = models.TextField()
    contact_date = models.DateTimeField(default = datetime.now)