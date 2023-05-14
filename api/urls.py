from django.urls import include, path
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()

# API URLs
router.register("contacts", api_views.ContactViewSet, basename="contact")

urlpatterns = [
    path('', include(router.urls)),
]
