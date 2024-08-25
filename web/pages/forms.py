from django import forms
from .models import Attende

class AttendeForm(forms.ModelForm):
    class Meta:
        model = Attende
        fields = ['nationality', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nationality'].empty_label = None
        self.fields['category'].empty_label = None

# class TickerTextForm(forms.ModelForm):
#     class Meta:
#         model = TickerText
#         fields = ['text', 'is_active']        