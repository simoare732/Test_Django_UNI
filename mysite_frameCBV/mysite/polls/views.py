from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import SearchForm, VoteForm, CreateQuestionForm, CreateChoiceForm
from .models import *


class PollListView(ListView):
    model = Question
    template_name = 'polls/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pub_date')[:20]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista di sondaggi"
        return context

class PollDetailView(DetailView):
    model = Question
    template_name =  "polls/detail.html"
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choices.all()
        return context


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get('search_string')
            where = form.cleaned_data.get('search_where')
            return redirect("polls:searchresults", sstring, where)

    else: form = SearchForm()

    return render(request, template_name="polls/searchpage.html", context={"form": form})

class SearchResultsView(ListView):
    model = Question
    template_name = "polls/searchresults.html"

    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs["sstring"]
        where = self.request.resolver_match.kwargs["where"]

        if "Question" in where:
            qq = Question.objects.filter(question_text__icontains=sstring)

        else:
            qc = Choice.objects.filter(choice_text__icontains=sstring)
            qq = Question.objects.none()
            for c in qc:
                qq |= Question.objects.filter(pk = c.question_id)

        return qq

def vote(request, pk):
    if request.method=='POST':
        print("Sono col post")
        form = VoteForm(data=request.POST, pk=pk)
        if form.is_valid():
            answer = form.cleaned_data.get('answer')
            return redirect('polls:votecasted', pk, answer.choice_text)

    else:
        #print("Sono col get")
        q = get_object_or_404(Question, pk=pk)
        form = VoteForm(pk=pk)
        return render(request, template_name="polls/vote.html", context={"form":form, "question":q})


class VoteCastedDetail(DetailView):
    model = Question
    template_name = "polls/votecasted.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "Answer"
        answer = self.request.resolver_match.kwargs["answer"]
        ctx["answer"] = answer
        correct = ctx["object"].choices.all().get(is_correct=True)
        if answer in correct.choice_text:
            ctx["message"] = "Right answer!"
        else:
            ctx["message"] = "Wrong answer! The right answer was " + str(correct.choice_text)

        try:
            c = ctx["object"].choices.all().get(choice_text=answer)
            c.votes += 1
            c.save()
        except Exception as e:
            print("Impossible to update vote value " + str(e))

        return ctx


class CreateQuestionView(CreateView):
    template_name =  "polls/createentry.html"
    form_class = CreateQuestionForm
    success_url = reverse_lazy("polls:index")

class CreateChoiceView(CreateView):
    template_name = "polls/createentry.html"
    form_class = CreateChoiceForm

    def get_success_url(self):
        ctx = self.get_context_data()
        pk = ctx["object"].question.pk
        return reverse("polls:detail", kwargs={"pk":pk})