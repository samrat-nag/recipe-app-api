from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileFeedItem (models.Model):
   username = models.OneToOneField(User,on_delete = models.CASCADE)
   ACC_class =models.IntegerField(default=0)
   status_text = models.CharField(max_length=50)
   created_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.status_text
