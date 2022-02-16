from django.db import models

class Payments(models.Model):
    user = models.CharField(max_length=100)
    amount = models.IntegerField(default=100)
