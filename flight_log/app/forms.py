from django import forms

class FlightLogForm(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'class': 'input-field',
        'id': 'start-time',
    }))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'class': 'input-field',
        'id': 'end-time',
    }))
    landings = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'class': 'input-field',
        'id': 'landings',
        'inputmode': 'numeric'
    }))