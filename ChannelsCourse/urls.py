from django.contrib import admin
from django.urls import path
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview),
]
