from rest_framework import permissions, viewsets

from app.plantTracker.serializers import (
    PlantSerializer,
    SpeciesSerializer,
    TransfersSerializer,
)
from app.plantTracker.models import Plant, Species, Transfers


class PlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Plant.objects.all().order_by("date_obtained")
    serializer_class = PlantSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Species.objects.all().order_by("generic_name")
    serializer_class = SpeciesSerializer


class TransfersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Transfers.objects.all().order_by("date")
    serializer_class = TransfersSerializer
