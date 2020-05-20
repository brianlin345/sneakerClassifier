from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_upload, name = 'index'),
    path('<image_name>', views.results, name = 'results')
]
