from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from .models import sneakerImage
from .forms import uploadSneakerImage, validateSneakerClassification

import os
from sneakerClassification.kerasClassifier import predict_image

def image_upload(request):
    if request.method == 'POST':
        sneakerImageForm = uploadSneakerImage(request.POST, request.FILES)
        if sneakerImageForm.is_valid():
            sneakerImage = sneakerImageForm.save()
            sneakerImage.sneaker_class = get_prediction(sneakerImage.sneaker_image.name)
            sneakerImage.sneaker_image_name = format_image_name(sneakerImage.sneaker_image.url)
            sneakerImage.save()

            return redirect('sneakerClassification:results', image_name = sneakerImage.sneaker_image_name)
    else:
        sneakerImageForm = uploadSneakerImage()
    context = {
        "form": sneakerImageForm
    }
    return render(request, "sneakerClassification/index.html", context)

def format_image_name(image_url):
    image_url = image_url.split(".", 1)[0]
    image_url = image_url.replace(settings.MEDIA_URL, "")
    image_url = image_url.split("/", 1)[1]
    return image_url

def get_prediction(image_name):
    shoe_dir = settings.MEDIA_ROOT
    return predict_image(shoe_dir, image_name)

def results(request, image_name):
    resultSneakerImage = sneakerImage.objects.get(sneaker_image_name = image_name)
    if request.method == 'POST':
        validateClassificationForm = validateSneakerClassification(request.POST)
        if validateClassificationForm.is_valid():
            validateSubmission = validateClassificationForm.cleaned_data['valid']
            resultSneakerImage.prediction_valid = validateSubmission
            resultSneakerImage.prediction_validated = True
            resultSneakerImage.save()

            return redirect('sneakerClassification:list')
    else:
        validateClassificationForm = validateSneakerClassification()
    context = {"sneaker_image": resultSneakerImage, "form": validateClassificationForm}
    return render(request, "sneakerClassification/result.html", context)

def list_results(request):
    context = {"sneaker_image_list": sneakerImage.objects.order_by('-upload_time')[:4]}
    return render(request, "sneakerClassification/list.html", context)
