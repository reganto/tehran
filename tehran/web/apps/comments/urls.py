from django.urls import path

from tehran.web.apps.comments import views

urlpatterns = [
    path("", views.index),
]