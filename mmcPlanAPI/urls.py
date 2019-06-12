from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.authenticate_user),
    path('user-profile/', views.get_user_profile),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]