
from django.contrib import admin
from django.urls import path, include
from django_q.monitor import monitor

from django_q.models import Schedule, Task

# admin.site.register(Schedule)
# admin.site.register(Task)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edwizy_app.urls')),
]

