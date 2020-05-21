from django.db import models
from django.forms import ModelForm
from datetime import datetime

class sneakerImage(models.Model):
    sneaker_class = models.CharField("class of this shoe given by sequential model", max_length = 100)
    sneaker_image = models.ImageField("image file for this shoe", upload_to='shoes')
    sneaker_image_name = models.CharField("name of image file for this shoe", max_length = 200)
    prediction_valid = models.BooleanField("user validation of prediction from model", default=False)
    prediction_validated = models.BooleanField("if prediction for image has been validated by user", default=False)
    upload_time = models.DateTimeField('date uploaded', default = datetime.now)


    def __str__(self):
        return "[" + "Classification: " + self.sneaker_class + ", Image Name: " + self.sneaker_image_name + "]"
