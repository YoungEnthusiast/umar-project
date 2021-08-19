from django.shortcuts import render
from .models import Category, Video
from .filters import VideoFilter
from django.core.paginator import Paginator
from .models import Video

def showVideos(request):
    context = {}
    videos = Video.objects.all()
    filtered_videos = VideoFilter(
        request.GET,
        queryset = Video.objects.all()
    )
    context['filtered_videos'] = filtered_videos
    paginated_filtered_videos = Paginator(filtered_videos.qs, 9)
    page_number = request.GET.get('page')
    videos_page_obj = paginated_filtered_videos.get_page(page_number)
    context['videos_page_obj'] = videos_page_obj
    total_videos = filtered_videos.qs.count()
    context['total_videos'] = total_videos
    return render(request, 'videos/videos.html', context=context)
