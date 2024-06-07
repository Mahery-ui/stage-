# Create your views here.
from .models import Question, Choice
from django.template import loader 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,request_id):
    response="You're looking at the resultsof question %s."
    return HttpResponse(response % question_id)

def vote(request,request_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk= request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error message': "You didn't select a choice",
              })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args= (question.id,)))


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    output= ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    template= loader.get_template('polls/index.html')
    context= {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})