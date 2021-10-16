# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index1, name = "index"),
    path("<str:name>", views.greet1, name = "greet"),
    path("fei", views.fei, name = "fei"),
    ]
