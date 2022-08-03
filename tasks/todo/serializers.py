from rest_framework import serializers 
from .models import Task 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'done', 'author', 'created', 'updated']
        read_only_fields = ['author']
    

    def create(self, validated_data):
        author = self.context['author']
        task = Task.objects.create(**validated_data)
        task.author = author 
        task.save()
        author.tasks.add(task)
        return validated_data



