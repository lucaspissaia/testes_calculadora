from django.forms import ModelForm
from django import forms

GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

# creating a form
class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)

'''class FormEscolha(forms.ModelForm):

    Sit = forms.ChoiceField(
        choices=((1, "Option one"), (2, "Option two"), (3, "Option three")),
        initial=(1,),
        widget=forms.ChoiceField,
    )

class CheckboxesSampleForm(forms.Form):
    checkboxes = forms.MultipleChoiceField(
        choices=((1, "Option one"), (2, "Option two"), (3, "Option three")),
        initial=(1,),
        widget=forms.CheckboxSelectMultiple,
    )
    alphacheckboxes = forms.MultipleChoiceField(
        choices=(("option_one", "Option one"), ("option_two", "Option two"), ("option_three", "Option three")),
        initial=("option_two", "option_three"),
        widget=forms.CheckboxSelectMultiple,
    )

    numeric_multiple_checkboxes = forms.MultipleChoiceField(
        choices=((1, "Option one"), (2, "Option two"), (3, "Option three")),
        initial=(1, 2),
        widget=forms.CheckboxSelectMultiple,
    )
'''