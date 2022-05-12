from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    price_per_unit = models.IntegerField()
    currency = models.CharField(max_length=200)
    currency_sgd = models.FloatField()
    price_sgd = models.FloatField()
    total_price_sgd = models.FloatField()
    moq = models.IntegerField(null=True)
    leadtime = models.CharField(max_length=250, null=True)
    remarks = models.CharField(max_length=250, null=True)
    update = models.CharField(max_length=250, null=True)


class Material(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class MaterialConfiguration(models.Model):
    name = models.ForeignKey(Material, on_delete=models.CASCADE)
    width1 = models.BooleanField(default=True)
    width2 = models.BooleanField(default=False)
    height = models.BooleanField(default=True)
    diameter1 = models.BooleanField(default=True)
    diameter2 = models.BooleanField(default=False)
    volume = models.BooleanField(default=False)
    weight = models.BooleanField(default=True)
    density = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    Formula = models.TextField(blank=True)

    def __str__(self):
        return self.name.name


class RFQEntry(models.Model):
    editor = models.ManyToManyField(User)
    rfq_no = models.CharField(max_length=300, unique=True)
    dwg_no = models.CharField(max_length=300)
    customer = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.rfq_no


class MaterialCost(models.Model):
    rfq_no = models.ForeignKey(RFQEntry, on_delete=models.CASCADE, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    width1 = models.FloatField(blank=True, null=True)
    width2 = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    diameter1 = models.FloatField(blank=True, null=True)
    diameter2 = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    editor = models.ManyToManyField(User)

    def __str__(self):
        return self.material.name


class ProcessCost(models.Model):
    rfq_no = models.ForeignKey(RFQEntry, on_delete=models.CASCADE)
    primary_process = models.ForeignKey(
        PrimaryProcess, on_delete=models.CASCADE)
    primary_cost = models.FloatField(blank=True, null=True)
    secondary_process = models.ForeignKey(
        SecondaryProcess, on_delete=models.CASCADE)
    secondary_cost = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True)
    editor = models.ManyToManyField(User)
