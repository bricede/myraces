from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.
class Race(models.Model):
    """A Race"""
    name = models.CharField(max_length = 100)
    date = models.DateField(default=date.today())
    category = models.CharField(max_length = 50)
    
    class category(models.TextChoices):
        TRAIL = 'TR', _('Trail')
        ULTRA = 'UL', _('Ultra')
        MARATHON = 'MA', _('Marathon')
        SEMI = 'SE', _('Semi')
        AUTRE = 'AU', _('Autre')
    
    category = models.CharField(
        max_length=2,
        choices = category.choices,
        default = category.TRAIL,
    )
    def __str__(self):
        return self.choices

    distance = models.SmallIntegerField()
    deniv = models.SmallIntegerField()
    time = models.CharField(max_length = 8)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """Returne a string representation of the model"""
        return self.name
