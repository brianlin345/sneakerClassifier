from django.forms import ModelForm
from .models import sneakerImage

class uploadSneakerImage(ModelForm):
    class Meta:
        model = sneakerImage
        fields = ['sneaker_image']
