from django import forms
from .models import Entry


class newEntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ["revenue", "revenuePerHour", 'bestBuyCards', 'totalTechSupport', 'geekSquadSolutions', 'officeAttach']
