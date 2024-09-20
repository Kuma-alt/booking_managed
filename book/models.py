from django.db import models
from django.contrib.auth.models import User

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.OneToOneField()
    with_kid = models.BooleanField()
    age = models.OneToOneField(int)

    ...
    
    class Meta:
        db_table = "passengers"
        verbose_name = "Regisetered Flight Passenger"


class Plane(models.Model):
    plane_brand = models.CharField(max_length=50)
    plane_model = models.CharField(max_length=50)

    class Meta():
        ordering = ["plane_brand", "plane_model"]


class Flight(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.SET_DEFAULT, default="unknown plane", related_name="flights")
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)


class PlaneSeat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Seat on the Flight"
        verbose_name_plural = "Seats on the Flight"
