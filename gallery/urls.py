from . import views
from django.urls import path


urlpatterns = [
    path('', views.ImageList.as_view(), name='gallery'),
]
