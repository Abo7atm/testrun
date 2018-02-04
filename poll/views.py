from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-publish_date')[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-publish_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'poll/index.html', context)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):

        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))


# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'poll/detail.html', {'question': question})

