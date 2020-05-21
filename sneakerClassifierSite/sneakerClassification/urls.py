from django.urls import path

from . import views

app_name = 'sneakerClassification'


urlpatterns = [
    path('', views.image_upload, name = 'index'),
    path('<image_name>/result', views.results, name = 'results'),
    path('list/', views.list_results, name = 'list')
]
