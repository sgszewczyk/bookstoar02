"""bookstoar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Imported AS to differentiate views meaning

from home import views as hviews
from myaccount import views as aviews
from browse import views as bviews
from myshelf import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hviews.home_view),
    path('home', hviews.home_view),
    path('browse', bviews.browse_view),
    path('myshelf', sviews.myshelf_view),
    path('myaccount', aviews.myaccount_view),
    ]
