from django.urls import path

from . import views

app_name = 'sneakerClassification'


urlpatterns = [
    path('', views.image_upload, name = 'index'),
    path('<image_name>', views.results, name = 'results')
]
