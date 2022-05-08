from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def browse_view(request):
    return render(request, 'browse/browse_view.html', {})