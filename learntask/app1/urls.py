from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from app1 import views

urlpatterns = [
    path('user/',views.user_objects.as_view()),
    path('user/<int:pk>/',views.user_objects_detail.as_view()),
    path('team/',views.team_objects.as_view()),
    path('team/<int:pk>/',views.team_objects_detail.as_view()),

]
urlpatterns=format_suffix_patterns(urlpatterns)