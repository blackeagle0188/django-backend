from django.urls import path
from django.contrib import admin
from render import views

from . import views

urlpatterns = [
    path('<int:month>/<int:day>', views.day_json_view),
]