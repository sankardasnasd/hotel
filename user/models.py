from django.db import models 
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4  ,editable=False,primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Amenities(Basemodel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name


class Hotel(Basemodel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models. TextField()
    amenities =models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name


class HotelImages(Basemodel):
    hotel= models.ForeignKey(Hotel ,related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotels")

    

    

class HotelBooking(Basemodel):
    hotel = models.ForeignKey(Hotel,related_name="hotel_booking",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_booking",on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booked_on = models.DateField(auto_now = True)
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))

class Package(Basemodel):
   
    package_name = models.CharField(max_length=50)
    Package_description = models.CharField(max_length=100)
    package_images = models.ImageField(upload_to="package")
   
    
    def __str__(self) -> str:
        return self.package_name 




