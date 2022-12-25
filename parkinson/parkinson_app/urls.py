from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_template, name='template'),
    path('control_parkinson/', views.control_parkinson, name='control_parkinson'),
    path('get_datas/', views.return_datas, name='get_datas'),
]