
from django.utils import timezone
from .models import index
from .models import about
from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')
def about(request):
    return render(request, 'blog/machines.html')
