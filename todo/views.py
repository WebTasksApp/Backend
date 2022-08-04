from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Task 
from .serializers import TaskSerializer
from django.contrib.auth import get_user_model


class TaskModelViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


    def get(self, request, pk=0):
        task = request.user.tasks.filter(pk=pk).first()
        if task:
            return Response(self.serializer_class(task).data)
        return Response(status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        tasks = request.user.tasks.all()
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'author': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
    

    def delete(self, request, pk=0):
        task = request.user.tasks.filter(pk=pk).first()
        if task:
            task.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def update(self, request, pk=0):
        task = request.user.tasks.filter(pk=pk).first()
        if task:
            serializer = self.serializer_class(task, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.validated_data)
        return Response(status=status.HTTP_404_NOT_FOUND)
        







        

        







