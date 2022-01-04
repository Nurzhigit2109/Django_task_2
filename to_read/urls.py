from django.urls import path, include
from to_read.views import to_read

urlpatterns = [
    path('', to_read, name='to_read')
]