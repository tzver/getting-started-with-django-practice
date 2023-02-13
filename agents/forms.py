from django import forms
from leads.models import Agent



class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
            # organisation will be pre-populized! Do not pass in the form
        )