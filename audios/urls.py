from django.urls import path
from . import views

urlpatterns = [
    path('audios', views.showAudios, name='audios'),
<<<<<<< HEAD
    path('a---n/audios', views.showAudiosFirst, name='audios_first'),
    path('a---n/audio/add-new', views.addAudio, name='audio_first'),
    path('a---n/audio-category/add-new', views.addCategory, name='audio_category_first'),
    path('a---n/audios/update/<int:id>', views.updateAudioFirst, name='audio_update_first'),
    path('a---n/audio-category/update/<int:id>', views.updateCategoryFirst, name='audio_category_update_first'),
    path('a---n/audios/delete/<int:id>', views.deleteAudioFirst),
    path('a---n/audio-category/delete/<int:id>', views.deleteCategoryFirst),
    path('a---n/audios-categories', views.showCategoriesFirst, name='audios_categories_first'),
=======

>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
]
