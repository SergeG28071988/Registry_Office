from .models import Marriage
from django.forms import ModelForm, TextInput, Textarea


class MarriageForm(ModelForm):
    class Meta:
        model = Marriage
        fields = ['groom', 'bride', 'marriage_date']
        widgets = {
            "groom": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите жениха'
            }),
            "bride": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите невесту'
            }),
            "marriage_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату заключения брака'
            }),    
        }
        