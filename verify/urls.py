from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.VerificationViewSet, 'faculty-verification')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('status/<str:task_id>/', views.TaskView.as_view(), name='task'),
]