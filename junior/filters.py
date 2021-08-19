import django_filters
from django_filters import CharFilter
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstFilter(django_filters.FilterSet):
    class Meta:
        model = FirstTerm
        fields = ['student', 'student__user__first_name', 'student__user__last_name', 'student__classe']

    def __init__(self, *args, **kwargs):
        super(FirstFilter, self).__init__(*args, **kwargs)
        self.filters['student'].label="Admission No"
        self.filters['student__classe'].label="Class"
        self.filters['student__user__first_name'].label="First Name"
        self.filters['student__user__last_name'].label="Last Name"
