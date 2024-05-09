from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class/', views.allClasses, name='class'),
    path('school/', views.allSchools, name='school'),
    path('answer/', views.allAnswers, name='answer'),
    path('assessment/', views.allAssessment, name='assessment'),
    path('award/', views.allAwards, name='award'),
]
