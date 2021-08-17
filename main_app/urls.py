from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mugs/', views.mugs_index, name='index'),
    path('mugs/<int:mug_id>/', views.mugs_detail, name='detail')
]