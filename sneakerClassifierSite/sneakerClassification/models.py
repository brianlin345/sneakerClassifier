from django.db import models
from django.forms import ModelForm

class sneakerImage(models.Model):
    sneaker_class = models.CharField("class of this shoe given by sequential model", max_length = 100)
    sneaker_image = models.ImageField("image file for this shoe", upload_to='shoes')
    sneaker_image_name = models.CharField("name of image file for this shoe", max_length = 200)
    prediction_valid = models.BooleanField("user validation of prediction from model")
    prediction_validated = models.BooleanField("if prediction for image has been validated by user")

    def __str__(self):
        return "[" + "Classification: " + self.sneaker_class + "Image Name: " + self.sneaker_image_name + "]"
