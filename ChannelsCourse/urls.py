from django.contrib import admin
from django.urls import path,include
from home.views import *
from chatapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview),
    path('chat/', chatView,name='chat'),
    path('login/', LoginView,name='login'),
    path('logout/', LogoutView,name='logout'),
    path('students/', generate_student_data),
]
