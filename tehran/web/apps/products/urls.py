from django.urls import path

from tehran.web.apps.products import views

urlpatterns = [
    path("", views.index),
]