from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_date = forms.DateField(label='Start Date',widget=DateInput)
    end_date = forms.DateField(label='End Date',widget=DateInput)

Sentiment= [
    (4,'+VE'),(2,'-VE'),(3,'Neutral')
    ]

class Sentiment(forms.Form):
    Sentiment= forms.CharField(label='Sentiment Choice ', widget=forms.Select(choices=Sentiment))