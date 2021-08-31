from django.contrib import admin
from django.urls import path
from home.views import *
from chatapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview),
    path('chat/', chatView),
    path('students/', generate_student_data),
]
