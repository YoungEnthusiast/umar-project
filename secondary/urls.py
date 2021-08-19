from django.urls import path
from . import views

urlpatterns = [
    path('staff/secondary/first-term', views.showFirsts, name='secondary_firsts'),
    path('parents/secondary/first-term', views.showFirstsUser, name='secondary_firsts_user'),
    path('staff/secondary/first-term/<int:pk>/', views.showFirst, name='secondary_show_first'),
    path('parents/secondary/first-term/<int:pk>/', views.showFirstUser, name='secondary_show_first_user'),
    path('staff/secondary/first-term/update/<int:id>', views.updateFirsts, name='secondary_firsts_update'),
    path('staff/secondary/first-term/add-scores', views.addFirst, name='secondary_first'),
    # path('staff/secondary/second-term', views.showSeconds, name='secondary_seconds'),
    # path('parents/secondary/second-term', views.showSecondsUser, name='secondary_seconds_user'),
    # path('staff/secondary/second-term/<int:pk>/', views.showSecond, name='secondary_show_second'),
    # path('parents/secondary/second-term/<int:pk>/', views.showSecondUser, name='secondary_show_second_user'),
    # path('staff/secondary/second-term/update/<int:id>', views.updateSeconds, name='secondary_seconds_update'),
    # path('staff/secondary/second-term/add-scores', views.addSecond, name='secondary_second'),
    # path('staff/secondary/third-term', views.showThirds, name='secondary_thirds'),
    # path('parents/secondary/third-term', views.showThirdsUser, name='secondary_thirds_user'),
    # path('staff/secondary/third-term/<int:pk>/', views.showThird, name='secondary_show_third'),
    # path('parents/secondary/third-term/<int:pk>/', views.showThirdUser, name='secondary_show_third_user'),
    # path('staff/secondary/third-term/update/<int:id>', views.updateThirds, name='secondary_thirds_update'),
    # path('staff/secondary/third-term/add-scores', views.addThird, name='secondary_third'),
]
