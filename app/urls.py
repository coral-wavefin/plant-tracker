from django.urls import include, path
from rest_framework import routers

from app.plantTracker import views

router = routers.DefaultRouter()
router.register(r"plants", views.PlantViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"transfers", views.TransfersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
