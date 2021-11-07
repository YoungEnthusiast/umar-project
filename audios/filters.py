import django_filters
from django_filters import CharFilter, DateFilter
<<<<<<< HEAD
from .models import Audio, Category
=======
from .models import Audio
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

class AudioFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    category__type = CharFilter(field_name='category__type', lookup_expr='icontains', label='Category')
    created = DateFilter(field_name="created", lookup_expr='gte', label='Date')

    class Meta:
        model = Audio
        fields = ['title', 'category__type', 'created']

    def __init__(self, *args, **kwargs):
        super(AudioFilter, self).__init__(*args, **kwargs)
        self.filters['category__type'].label="Category"
<<<<<<< HEAD

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['category']
=======
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
