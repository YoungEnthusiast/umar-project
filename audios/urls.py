from django.urls import path
from . import views

urlpatterns = [
    path('audios', views.showAudios, name='audios'),
    path('a---n/audios', views.showAudiosFirst, name='audios_first'),
    path('a---n/audio/add-new', views.addAudio, name='audio_first'),
    path('a---n/audios/update/<int:id>', views.updateAudioFirst, name='audio_update_first'),
    path('a---n/audios/delete/<int:id>', views.deleteAudioFirst),
    path('a---n/audios_categories', views.showCategoriesFirst, name='audios_categories_first'),
]
