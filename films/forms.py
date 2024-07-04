from .models import Film
from django import forms

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'description', 'review')
