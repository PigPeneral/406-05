from . import views
from django.views import debug
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("Django API is working! 🚀")


urlpatterns = [
    path('debug/', debug.default_urlconf),
    path('', views.index_view, name='index'),
    path('admin/', admin.site.urls),
    path('api/', api_home, name='api_home'),
]