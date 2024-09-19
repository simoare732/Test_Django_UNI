from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
    CHOICE_LIST = [("Titolo", "Cerca tra i titoli"), ("Autore", "Cerca tra gli autori")]
    helper = FormHelper()
    helper.form_id = "search_crispy_form"
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Cerca'))
    search_string = forms.CharField(
        label='Cerca qualcosa',
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    search_where = forms.ChoiceField(
        label='Dove?',
        required=True,
        choices=CHOICE_LIST,
        widget=forms.Select(attrs={'class': 'form-select'})
    )