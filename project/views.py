from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
# Create your views here.
def proDetail(request, id):
    pD = Project.objects.get(project_id = id)
    return render(request, 'home/project-details.html', {'pD':pD})