from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Race

def index(request):
    return render(request, 'races/index.html')

# Liste des courses
@login_required
def race_list(request):
    races_list = Race.objects.order_by('-date')
    context = {'races_list': races_list}
    return render(request, 'races/race_list.html', context)

# Détails d'une course
@login_required
def detail(request, race_id):
    race = get_object_or_404(Race, pk = race_id)
    return render(request, 'races/detail.html', {'race': race})

