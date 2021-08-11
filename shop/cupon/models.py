from django.db import models

# Create your models here.
class cupon(models.Model):
    off_code = models.CharField(max_length=15)
    off = models.DecimalField(max_digits=2, decimal_places=0)
    member = models.IntegerField(default=0)
    