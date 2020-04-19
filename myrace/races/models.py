from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.
class Race(models.Model):
    """A Race"""
    race_name = models.CharField(max_length = 100)
    race_date = models.DateField(default=date.today())
    race_category = models.CharField(max_length = 50)
    
    class race_category(models.TextChoices):
        TRAIL = 'TR', _('Trail')
        ULTRA = 'UL', _('Ultra')
        MARATHON = 'MA', _('Marathon')
        SEMI = 'SE', _('Semi')
        AUTRE = 'AU', _('Autre')
    
    race_category = models.CharField(
        max_length=2,
        choices=race_category.choices,
        default=race_category.TRAIL,
    )

    race_distance = models.SmallIntegerField()
    race_deniv = models.SmallIntegerField()
    race_time = models.CharField(max_length = 8)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Returne a string representation of the model"""
        return self.race_name
