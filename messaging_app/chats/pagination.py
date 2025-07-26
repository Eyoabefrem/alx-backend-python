from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'  # Optional: allow changing page size via query
    max_page_size = 100  # Prevent overly large pages
