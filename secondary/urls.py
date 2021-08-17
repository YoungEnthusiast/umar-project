from django.urls import path
from . import views

urlpatterns = [
    path('staff/secondary/first-term', views.showFirsts, name='secondary_firsts'),
]
