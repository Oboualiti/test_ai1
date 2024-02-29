from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name="home" ),
    path('result_template/', views.result_template , name="result_template" ),
    path('input_form/', views.input_form , name="input_form" ),

]