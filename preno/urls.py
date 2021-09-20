from django.urls import path
from . import views

app_name = 'preno'

urlpatterns = [
    path('', views.index, name='index'),
    path('curso/<curso>/', views.curso, name='curso')
]