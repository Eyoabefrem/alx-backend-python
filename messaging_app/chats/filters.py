import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sent_after = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_before = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')
    user = django_filters.NumberFilter(field_name='sender__id')  # or sender__username

    class Meta:
        model = Message
        fields = ['sent_after', 'sent_before', 'user']
