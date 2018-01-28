from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)


def question(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response%question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'poll/detail.html', {'question': question})

