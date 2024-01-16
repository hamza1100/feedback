from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.CharField(max_length=500)
    rating = models.IntegerField()
    # rating = models.IntegerField([MinValueValidator(1), MaxValueValidator(5)])
