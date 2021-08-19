import django_filters
from django_filters import CharFilter
from .models import News

class NewsFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Headline')
    content = CharFilter(field_name='content', lookup_expr='icontains', label='Content')

    class Meta:
        model = News
        fields = ['headline', 'content', 'created']

    def __init__(self, *args, **kwargs):
        super(NewsFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
