from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Category(models.Model):
    """Catégorie de courses : trail, ultra, marathon, semi, autre... """
    text = models.CharField(max_length = 50, null = True)
    
    def __str__(self):
        return self.text

class Runner(models.Model):
    """liste des courreurs"""
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    dateofbirth = models.DateField()
    
    def __str__(self):
        return self.firstname

class Race(models.Model):
    """A Race"""
    name = models.CharField(max_length = 100)
    date = models.DateField(default=date.today())
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    runner = models.ForeignKey(Runner, on_delete = models.CASCADE)
    distance = models.PositiveSmallIntegerField(null = True)
    deniv = models.PositiveSmallIntegerField(null = True)
    time = models.CharField(max_length = 8, null = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Returne a string representation of the model"""
        return self.name

