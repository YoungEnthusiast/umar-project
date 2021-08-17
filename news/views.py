from django.shortcuts import render
from .models import News
from .filters import NewsFilter
from django.core.paginator import Paginator

def showEvents(request):
    context = {}
    news = News.objects.all()
    filtered_news = NewsFilter(
        request.GET,
        queryset = News.objects.all()
    )

    context['filtered_news'] = filtered_news
    paginated_filtered_news = Paginator(filtered_news.qs, 10)
    page_number = request.GET.get('page')
    news_page_obj = paginated_filtered_news.get_page(page_number)
    context['news_page_obj'] = news_page_obj
    total_news = filtered_news.qs.count()
    context['total_news'] = total_news
    return render(request, 'news/events.html', context=context)
