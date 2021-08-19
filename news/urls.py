from django.urls import path
from . import views
#from treatment import views as treatment_views

urlpatterns = [
    path('news-and-events', views.showEvents, name='events'),
]
