from django.urls import path
from .views import upload_csv, homepage

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('', homepage, name='homepage'),
]