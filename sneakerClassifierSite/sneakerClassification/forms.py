from django import forms
from django.forms import ModelForm
from .models import sneakerImage

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class uploadSneakerImage(ModelForm):
    sneaker_image = forms.ImageField(label='')

    class Meta:
        model = sneakerImage
        fields = ['sneaker_image']

class validateSneakerClassification(forms.Form):
    valid = forms.ChoiceField(choices = BOOL_CHOICES, label="", 
                              initial='', widget=forms.Select(), required=True)
