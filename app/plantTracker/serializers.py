from app.plantTracker.models import Species, Plant, Transfers
from rest_framework import serializers


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = [
            "alias",
            "price",
            "date_obtained",
            "date_died",
            "source",
            "parent",
            "species",
            # "external_api_data",
        ]


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"


class TransfersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfers
        fields = ["plant_id", "date", "price", "new_owner"]
