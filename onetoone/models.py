from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=80)
    address=models.CharField(max_length=80)
    def __str__(self):
        return f"{ self.name}"
class Restaurant(models.Model):
  place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
  serve_pizaa=models.BooleanField(default=False)
  serve_hotdog=models.BooleanField(default=False)
  def __str__(self):
     return f"  {self.place.name}"
class Waiter(models.Model):
   restaurant= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)

   def __str__(self):
      return f"In {self.restaurant} waiter is {self.name} "