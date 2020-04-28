from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Race
from .forms import SearchForm

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

# Recherche d'une course
@login_required
def search_results(request):
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = SearchForm()
    else:
        # Post data submitted, process data
        form = SearchForm(data=request.POST)
        #print(form['value'])
        if form.is_valid():
            txt = form.cleaned_data['search_txt']
            queryset = Race.objects.filter(name__icontains = txt)
            return render(request, 'races/search_results.html', {'queryset': queryset})
    
    # Display a blank form
    context = {'form': form}
    return render(request, 'races/search_results.html', context)
    