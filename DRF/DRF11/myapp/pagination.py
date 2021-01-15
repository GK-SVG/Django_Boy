from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class StudentPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7

class StudentLimitffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 7