from django.db import models
from django.contrib.auth.models import User

class hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_des=models.TextField()
    reviews=models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='photo/', null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def  __str__(self) -> str:
        return  str.title
class room(models.Model):
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    room_number=models.IntegerField(unique=True)
    room_type=models.CharField(max_length=100)
    price_per_night=models.IntegerField()
    is_available=models.BooleanField(default=True)
    room_des=models.TextField(default="")
    # room_pic=models.ImageField(upload_to='photo/',null=True,blank=True)

    def __str__(self) -> str:
        return f"Room{self.room_number}({self.room_type})"
    
class book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE,null=True,default=1)
    room=models.ForeignKey(room,on_delete=models.CASCADE,null=True)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    number_of_guest=models.IntegerField()
    booking_date=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return {self.hotel.hotel_name}
class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=15)
    is_vendor=models.BooleanField(default=False)
    def __str__(self):
        return super().__str__()
class RoomImage(models.Model):
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    room_pic = models.ImageField(upload_to='photo/')
    
    def __str__(self) -> str:
        return f"Image for Room {self.room.room_number}"
  






