from django.urls import path
from . import views

urlpatterns = [

    path('employe/', views.EmployeAPIVIEW.as_view()),
]