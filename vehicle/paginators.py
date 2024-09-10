from rest_framework.pagination import PageNumberPagination


class VehiclePagination(PageNumberPagination):
    page_size = 10