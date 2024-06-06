# Create your views here.
from .models import Question, Choice 
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

    
class IndexView(generic.ListView):
    template_name= 'polls/index.html'
    contex_object_name= 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model= Question
    template_name= 'polls/detail_html'

class ResultsView(generic.DateDetailView):
    model= Question
    template_name= 'polls/results.html'

def vote(request,request_id):
    return HttpResponseRedirect("You're voting on question %s." % question_id) 

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't sselect a choice",
                                                     })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))