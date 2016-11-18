from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice, QuestionPost
from .forms import QuestionForm, QuestionPostForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('archive') == "True":
            return Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')

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
    form_class = QuestionPostForm()
    print(model)

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        context['question_comments'] = QuestionPost.objects.filter(
            question=self.get_object()
        ).order_by('-post_date')[:5]
        context['form'] = self.form_class
        return context


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
        if request.session.get('has_voted{%s}' % p.pk, False):
            return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': "You have already voted",
            })
        selected_choice.votes += 1
        selected_choice.save()
        request.session['has_voted{%s}' % p.pk] = True
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def addpoll(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = Question.objects.create(
                question_text=form.cleaned_data['question_title'],
                pub_date=timezone.now())
            Choice.objects.create(question=question,
                                  choice_text=form.cleaned_data['answer1'])
            Choice.objects.create(question=question,
                                  choice_text=form.cleaned_data['answer2'])
            if form.cleaned_data['answer3'] != "":
                Choice.objects.create(question=question,
                                      choice_text=form.cleaned_data['answer3'])
            request.session['has_created'] = question.pk
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return render(request, 'polls/addpoll.html', {
                'error_message': "Seems you didn't put all the necessary data",
                'questionform': form,
            })
        return render(request, 'polls/addpoll.html', {'questionform': form})

    else:
        form = QuestionForm()
        return render(request, 'polls/addpoll.html', {'questionform': form})


def deletepoll(request, pk):
    p = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        if request.session.get('has_created') == p.pk:
            p.delete()
        else:
            return render(request, 'polls/detail.html', {
                'question': p,
                'error_message':
                "You do not have permissions to delete this poll",
            })
        return HttpResponseRedirect(reverse('polls:index'))
    return render(request, 'polls/deletepoll.html', {'pk': pk})


def addpost(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionPostForm(data=request.POST)
        if form.is_valid():
            QuestionPost.objects.create(
                question=q,
                post_date=timezone.now(),
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
            )
            return HttpResponseRedirect(reverse('polls:results',
                                        args=(q.id,)))
        else:
            return render(request, 'polls/results.html', {
                'question': q,
                'error_message':
                "Your post is invalid",
                'form': form,
            })
    else:
        return HttpResponseRedirect(reverse('polls:results',
                                    args=(q.id,)))
