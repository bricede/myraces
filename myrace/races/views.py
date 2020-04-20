from django.shortcuts import render

from .models import Race

# Liste des courses
def index(request):
    races_list = Race.objects.order_by('-date')
    context = {'races_list': races_list}
    return render(request, 'races/index.html', context)





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     #question = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})