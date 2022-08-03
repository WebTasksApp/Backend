from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('tasks', views.TaskModelViewSet, basename='tasks')


urlpatterns = [
    path('', views.TaskModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', views.TaskModelViewSet.as_view({'get': 'get', 'delete': 'delete', 'patch': 'update'}))
]
urlpatterns += router.urls