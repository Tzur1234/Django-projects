from django.urls import path
from . import views

urlpatterns = [
    # path("<str:name>", views.index, name="index"),
    path("", views.greet, name="greet"),
    path("1", views.func1, name="func1")
]