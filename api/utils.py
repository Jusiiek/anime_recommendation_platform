from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PaginatedListMixin:
    pagination_class = CustomPagination

    def paginate(self, queryset, request):
        paginator = self.pagination_class()

        if 'perPage' in request.GET.keys():
            paginator.per_page = request.GET['perPage']

        page = paginator.paginate_queryset(queryset=queryset, request=request)
        serialzer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response(serialzer.data)
