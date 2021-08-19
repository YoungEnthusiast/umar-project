from django.urls import path
from . import views

urlpatterns = [
    path('staff/junior/first-term', views.showFirsts, name='junior_firsts'),
    path('parents/junior/first-term', views.showFirstsUser, name='junior_firsts_user'),
    path('staff/junior/first-term/<int:pk>/', views.showFirst, name='junior_show_first'),
    path('parents/junior/first-term/<int:pk>/', views.showFirstUser, name='junior_show_first_user'),
    path('staff/junior/first-term/update/<int:id>', views.updateFirsts, name='junior_firsts_update'),
    path('staff/junior/first-term/add-scores', views.addFirst, name='junior_first'),
    # path('staff/junior/second-term', views.showSeconds, name='junior_seconds'),
    # path('parents/junior/second-term', views.showSecondsUser, name='junior_seconds_user'),
    # path('staff/junior/second-term/<int:pk>/', views.showSecond, name='junior_show_second'),
    # path('parents/junior/second-term/<int:pk>/', views.showSecondUser, name='junior_show_second_user'),
    # path('staff/junior/second-term/update/<int:id>', views.updateSeconds, name='junior_seconds_update'),
    # path('staff/junior/second-term/add-scores', views.addSecond, name='junior_second'),
    # path('staff/junior/third-term', views.showThirds, name='junior_thirds'),
    # path('parents/junior/third-term', views.showThirdsUser, name='junior_thirds_user'),
    # path('staff/junior/third-term/<int:pk>/', views.showThird, name='junior_show_third'),
    # path('parents/junior/third-term/<int:pk>/', views.showThirdUser, name='junior_show_third_user'),
    # path('staff/junior/third-term/update/<int:id>', views.updateThirds, name='junior_thirds_update'),
    # path('staff/junior/third-term/add-scores', views.addThird, name='junior_third'),
]
