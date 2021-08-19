from django.urls import path
from . import views

urlpatterns = [
    path('audios', views.showAudios, name='audios'),

]
