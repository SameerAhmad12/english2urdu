from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
    path("index",views.index, name = "index"),
    path("about",views.about, name ="about")
]
