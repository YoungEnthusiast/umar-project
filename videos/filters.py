import django_filters
from django_filters import CharFilter, DateFilter
from .models import Video

class VideoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    category__type = CharFilter(field_name='category__type', lookup_expr='icontains', label='Category')
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Video
        fields = ['title', 'category__type', 'created']

    def __init__(self, *args, **kwargs):
        super(VideoFilter, self).__init__(*args, **kwargs)
        self.filters['category__type'].label="Category"
