from django.urls import path
from . import views

urlpatterns = [
    path('staff/nursery/first-term', views.showFirsts, name='nursery_firsts'),
    #path('parents/nursery/first-term', views.showFirstsUser, name='nursery_firsts_user'),
    path('staff/nursery/first-term/<int:pk>/', views.showFirst, name='nursery_show_first'),
    # path('parents/nursery/first-term/<int:pk>/', views.showFirstUser, name='nursery_show_first_user'),
    path('staff/nursery/first-term/update/<int:id>', views.updateFirsts, name='nursery_firsts_update'),
    path('staff/nursery/first-term/add-scores', views.addFirst, name='nursery_first'),
    # path('staff/nursery/second-term', views.showSeconds, name='nursery_seconds'),
    # path('parents/nursery/second-term', views.showSecondsUser, name='nursery_seconds_user'),
    # path('staff/nursery/second-term/<int:pk>/', views.showSecond, name='nursery_show_second'),
    # path('parents/nursery/second-term/<int:pk>/', views.showSecondUser, name='nursery_show_second_user'),
    # path('staff/nursery/second-term/update/<int:id>', views.updateSeconds, name='nursery_seconds_update'),
    # path('staff/nursery/second-term/add-scores', views.addSecond, name='nursery_second'),
    # path('staff/nursery/third-term', views.showThirds, name='nursery_thirds'),
    # path('parents/nursery/third-term', views.showThirdsUser, name='nursery_thirds_user'),
    # path('staff/nursery/third-term/<int:pk>/', views.showThird, name='nursery_show_third'),
    # path('parents/nursery/third-term/<int:pk>/', views.showThirdUser, name='nursery_show_third_user'),
    # path('staff/nursery/third-term/update/<int:id>', views.updateThirds, name='nursery_thirds_update'),
    # path('staff/nursery/third-term/add-scores', views.addThird, name='nursery_third'),
]
