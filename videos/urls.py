from django.urls import path
from . import views

urlpatterns = [
    path('videos', views.showVideos, name='videos'),
<<<<<<< HEAD
    path('a---n/video/add-new', views.addVideo, name='video_first'),
    path('a---n/gallery', views.showVideosFirst, name='videos_first'),
    path('a---n/categories', views.showCategoriesFirst, name='categories_first'),
    path('a---n/category/add-new', views.addCategory, name='category_first'),
    path('a---n/gallery/update/<int:id>', views.updateVideoFirst, name='video_update_first'),
    path('a---n/category/update/<int:id>', views.updateCategoryFirst, name='category_update_first'),
    path('a---n/gallery/delete/<int:id>', views.deleteVideoFirst),
    path('a---n/category/delete/<int:id>', views.deleteCategoryFirst),
=======
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
]
