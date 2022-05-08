from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myaccount_view(request):
    return render(request, 'myaccount/myaccount_view.html', {})