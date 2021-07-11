from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'http://127.0.0.1:8000/drf/task-list/',
		'Detail View':'http://127.0.0.1:8000/drf/task-detail/<str:pk>/',
		'Create':'http://127.0.0.1:8000/drf/task-create/',
		'Update':'http://127.0.0.1:8000/drf/task-update/<str:pk>/',
		'Delete':'http://127.0.0.1:8000/drf/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request, pk):
    taskdetail = Task.objects.get(id=pk)
    serializer = TaskSerializer(taskdetail, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("task deleted successfully!")
