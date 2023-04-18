from django.urls import include, path
from articles import views

urlpatterns = [
    path('index/', views.index, name="index"),
]
