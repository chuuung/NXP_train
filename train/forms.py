from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["OtherRequest"]
        labels = {
            "OtherRequest": ("Other Request"),
        }
    
    '''widgets = {
        '': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'})
    }'''