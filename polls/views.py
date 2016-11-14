from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the voting form
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def addpoll(request):
    return render(request, 'polls/addpoll.html')


def addpollpost(request):
    if request.POST['question_title'] != "":
        question = Question.objects.create(question_text=request.POST
                                           ['question_title'],
                                           pub_date=timezone.now())
    if request.POST['1'] != "":
        Choice.objects.create(question=question, choice_text=request.POST['1'])
    if request.POST['2'] != "":
        Choice.objects.create(question=question, choice_text=request.POST['2'])
    if request.POST['3'] != "":
        Choice.objects.create(question=question, choice_text=request.POST['3'])
    return HttpResponseRedirect(reverse('polls:index'))
