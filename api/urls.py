from django.urls import path
from .views import *

urlpatterns = [
    path('get_record', get_record),
    ]