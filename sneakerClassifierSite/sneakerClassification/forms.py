from django import forms
from django.forms import ModelForm
from .models import sneakerImage

class uploadSneakerImage(ModelForm):
    sneaker_image = forms.ImageField(label='')

    class Meta:
        model = sneakerImage
        fields = ['sneaker_image']

class validateSneakerClassification(forms.Form):
    valid = forms.BooleanField()
