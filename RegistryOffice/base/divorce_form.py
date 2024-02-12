from .models import Divorce
from django.forms import ModelForm, TextInput, Textarea


class DivorceForm(ModelForm):
    class Meta:
        model = Divorce
        fields = ['husband', 'wife', 'divorce_date']
        widgets = {
            "husband": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите мужа'
            }),
            "wife": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите жену'
            }),
            "divorce_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату развода'
            }),    
        }
        