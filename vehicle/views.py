from rest_framework import viewsets

from vehicle.models import Car
from vehicle.serilazers import CarSerializer


class CarViewSet(viewsets.ViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
