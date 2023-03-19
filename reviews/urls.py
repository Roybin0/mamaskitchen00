from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path('new-review', views.review, name='new-review'),
]