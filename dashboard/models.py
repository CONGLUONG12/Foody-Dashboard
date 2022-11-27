from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Vendor(models.Model):
    ReviewUrl = models.CharField(max_length=500, null=False)
    RestaurantId = models.CharField(max_length=100, primary_key=True, editable=False)
    Name = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=200, null=True)
    District = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=50, null=True)
    RestaurantStatus = models.FloatField(null=True)
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    TotalReviews = models.FloatField(null=True)
    nExcellentReviews = models.FloatField(null=True)
    nGoodReviews = models.FloatField(null=True)
    nAverageReviews = models.FloatField(null=True)
    nBadReviews = models.FloatField(null=True)
    LocationScore = models.FloatField(null=True)
    PriceScore = models.FloatField(null=True)
    QualityScore = models.FloatField(null=True)
    ServingScore = models.FloatField(null=True)
    SpaceScore = models.FloatField(null=True)
    AvgScore = models.FloatField(null=True)
    TotalPictures = models.FloatField(null=True)
    TotalViews = models.FloatField(null=True)
    TotalSaves = models.FloatField(null=True)
    IsBooking = models.BooleanField(null=True)
    IsDelivery = models.BooleanField(null=True)
    PrepTime = models.CharField(max_length=20, null=True)
    Capacity = models.CharField(max_length=50, null=True)
    LastHourCustomer = models.TextField(null=True)
    ExtraInfo = models.TextField(null=True)
    Active = models.BooleanField(null=True)
    TotalFavourites = models.FloatField(null=True)
    TotalCheckIns = models.FloatField(null=True)
    categories = models.TextField(null=True)
    cuisines = models.CharField(max_length=100, null=True)
    avg = models.FloatField(null=True)
    service_fee = models.FloatField(null=True)
    avg_price = models.FloatField(null=True)
    min_order_value = models.FloatField(null=True)
    min_charge = models.FloatField(null=True) # need pre-process
    minimum_shiping_fee = models.FloatField(null=True) # need pre-process
    is_foody_delivery = models.BooleanField(null=True) # need pre-process
    min_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True)
    min_order_amount = models.TextField(null=True) # need pre-process
    expired = models.TextField(null=True)
    promo_description = models.TextField(null=True)
    promo_code = models.TextField(null=True)
    max_discount_value = models.TextField(null=True) # need pre-process
    max_usage_time = models.TextField(null=True)
    apply_order = models.TextField(null=True)
    all_reviews = models.TextField(null=True)
    seeding_pct = models.TextField(null=True)


class Chart(models.Model):
    name = models.CharField(max_length=200) 
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    finish_date = models.DateField()

    #string representation method
    def __str__(self):
        return str(self.name)

    #overiding the save method
    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)
