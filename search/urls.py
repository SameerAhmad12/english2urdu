from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
    path('word1',views.word1,name="word1"),
    path("index",views.index, name = "index"),
    path("about",views.about, name ="about")
]
