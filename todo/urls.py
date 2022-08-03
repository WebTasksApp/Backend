from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('tasks', views.TaskModelViewSet, basename='tasks')


urlpatterns = [
    path('tasks', views.TaskModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
    path('task/<int:pk>', views.TaskModelViewSet.as_view({'get': 'get', 'delete': 'delete', 'patch': 'update'}), name='task')
]
urlpatterns += router.urls