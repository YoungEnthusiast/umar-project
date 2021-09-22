import django_filters
from django_filters import CharFilter
from .models import First

class FirstFilter(django_filters.FilterSet):
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = First
        fields = ['session', 'subject']

    # def __init__(self, *args, **kwargs):
    #     super(FirstFilter, self).__init__(*args, **kwargs)
    #     self.filters['student__role'].label="Admission No"
    #     self.filters['student__classe'].label="Class"
    #     self.filters['student__user__first_name'].label="First Name"
    #     self.filters['student__user__last_name'].label="Last Name"


class FirstFilter2(django_filters.FilterSet):
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = First
        fields = ['session']

class FirstFilterPay(django_filters.FilterSet):
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = First
        fields = ['session', 'student__classe']

    def __init__(self, *args, **kwargs):
        super(FirstFilterPay, self).__init__(*args, **kwargs)
        self.filters['student__classe'].label="Class"
