from django.db import models
from django.contrib.auth.models import User
class hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_des=models.TextField()
    reviews=models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def  __str__(self) -> str:
        return  str.title



