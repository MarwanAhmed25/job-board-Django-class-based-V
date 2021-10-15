from django.urls import path
from .views import *

app_name='jobs'
urlpatterns = [
    path('', JobList.as_view(), name='all'),
    path('create/', JobCreate.as_view(), name='create'),
    path('<str:slug>/edit/', JobUpdate.as_view(), name='update'),
    path('<str:slug>/delete/', JobDelete.as_view(), name='delete'),
    path('<str:slug>/', JobDetail.as_view(), name='detail'),
    
]
