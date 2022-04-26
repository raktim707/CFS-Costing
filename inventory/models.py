from django.db import models

# Create your models here.


class Material(models.Model):
    name = models.CharField(max_length=200)
    width1 = models.BooleanField(default=True)
    width2 = models.BooleanField(default=False)
    height = models.BooleanField(default=True)
    diameter1 = models.BooleanField(default=True)
    diameter2 = models.BooleanField(default=False)
    volume = models.BooleanField(default=False)
    weight = models.BooleanField(default=True)
    density = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    Formula = models.CharField(blank=True, max_length=550)

    def __str__(self):
        return self.name


class PrimaryProcess(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SecondaryProcess(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class StandardPart(models.Model):
    dwg_no = models.IntegerField()
    rev = models.CharField(max_length=200)
    det_no = models.CharField(max_length=250)
    Manufacturer = models.CharField(max_length=250)
    model_no = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.IntegerField()
    currency = models.CharField(max_length=200)
    currency_sgd = models.FloatField()
    price_sgd = models.FloatField()
    total_price_sgd = models.FloatField()
