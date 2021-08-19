from django.shortcuts import render
from .models import Category, Audio
from .filters import AudioFilter
from django.core.paginator import Paginator
from .models import Audio

def showAudios(request):
    context = {}
    audios = Audio.objects.all()
    filtered_audios = AudioFilter(
        request.GET,
        queryset = Audio.objects.all()
    )
    context['filtered_audios'] = filtered_audios
    paginated_filtered_audios = Paginator(filtered_audios.qs, 9)
    page_number = request.GET.get('page')
    audios_page_obj = paginated_filtered_audios.get_page(page_number)
    context['audios_page_obj'] = audios_page_obj
    total_audios = filtered_audios.qs.count()
    context['total_audios'] = total_audios
    return render(request, 'audios/audios.html', context=context)
