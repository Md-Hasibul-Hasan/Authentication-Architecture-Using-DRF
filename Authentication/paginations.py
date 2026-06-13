from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# PageNumberPagination → Admin panel, normal CRUD, small–medium data
class MyPageNumberPagination(PageNumberPagination):
    page_size = 2 # records per page
    max_page_size = 10  # max records per page
    page_query_param = 'page' # /?page=1 default
    page_size_query_param = 'records' # /?page=1&records=5
    last_page_strings = ['last', 'end'] # /?page=last


# LimitOffsetPagination → Mobile app, infinite scroll / “load more” UI
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit' # /?limit=5
    offset_query_param = 'offset' # /?limit=5&offset=5


# CursorPagination → Large dataset, high-traffic production, frequently changing data
class MyCursorPagination(CursorPagination):
    page_size = 2
    max_page_size = 10
    page_size_query_param = 'page_size'
    cursor_query_param = 'cursor'
    ordering = '-id'