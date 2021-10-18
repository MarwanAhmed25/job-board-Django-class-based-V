from django.urls import path
from .views import *
app_name = 'profiles'
urlpatterns = [
    path('', ProfileList.as_view(), name='all'),
    path('<str:slug>/', ProfileDetail.as_view(), name='detail'),
    path('<str:slug>/edit/', profile_update, name='update'),
    path('<str:slug>/delete/', ProfileDelete.as_view(), name='delete'),

]
