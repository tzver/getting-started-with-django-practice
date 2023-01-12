from django import forms

class LeadForm(forms.Form): #inherit from forms.Form
    # give fields of a form
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)