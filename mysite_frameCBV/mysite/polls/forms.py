from django import forms
from django.shortcuts import get_object_or_404

from .models import *

class SearchForm(forms.Form):
    CHOICE_LIST = [("Questions", "Search in Questions"),
                   ("Choiches", "Search in Choiches")]

    search_string = forms.CharField(label="Search String", max_length=100, min_length=3, required=True)
    search_where = forms.ChoiceField(label="Search where", required=True, choices = CHOICE_LIST)

class VoteForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=None, required=True, label="Select your f****** answer!")

    def __init__(self, pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        q = get_object_or_404(Question, pk=pk)
        self.fields['answer'].queryset = q.choices.all()


class CreateQuestionForm(forms.ModelForm):
    description = "Create a new question"

    def clean(self):
        if len(self.cleaned_data["question_text"]) < 5:
            self.add_error('question_text', "Error: Question must be at least 5 characters long!")

        return self.cleaned_data

    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
            "pub_date": forms.DateInput(format=("%d%m%Y"), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type':'date'})
        }

class CreateChoiceForm(forms.ModelForm):
    description = "Create a new choices for a question"

    def clean(self):
        q = get_object_or_404(Question, pk=self.cleaned_data["question"].id)

        choices = q.choices.all()
        choices_false = choices.filter(is_correct = False)

        if choices.count() == 4:
            self.add_error('question', "Error: Question already has 4 options")
        elif choices.count() == 3:
            self.add_error('is_correct', 'Error: exactly one choice must be correct')

        if choices.filter(is_correct = True).count() == 1 and self.cleaned_data["is_correct"] == True:
            self.add_error('is_correct', "Error: This question already has a correct answer")

        return self.cleaned_data

    class Meta:
        model = Choice
        fields = "__all__"
