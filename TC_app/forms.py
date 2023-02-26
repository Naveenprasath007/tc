from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)


S1= [
    ('sortaz','ascending'),('sortza','descending'),
    ]

class Sot(forms.Form):
    S= forms.CharField(label='Sort By', widget=forms.Select(choices=S1))