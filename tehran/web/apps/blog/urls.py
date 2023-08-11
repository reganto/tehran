from django.urls import path

from tehran.web.apps.blog import views

urlpatterns = [
    path("", views.index),
]