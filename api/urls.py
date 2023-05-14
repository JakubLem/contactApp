from django.urls import include, path
from rest_framework import routers
from api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

# API URLs
router.register("contacts", api_views.ContactViewSet, basename="contacts")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', api_views.UserLoginView.as_view(), name='login'),
    path('logout/', api_views.UserLogoutView.as_view(), name='logout'),
    path('registration/', api_views.UserRegistrationView.as_view(), name='registration'),
    path('api/auth/registration/', api_views.RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', obtain_auth_token, name='api_token_auth'),
    path('contact/', api_views.contact, name='contact'),
]
