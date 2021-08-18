from django.urls import path
# from mugs.views import MugList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mugs/', views.mugs_index, name='index'),
    path('mugs/<int:mug_id>/', views.mugs_detail, name='detail'),
    path('mugs/create/', views.MugCreate.as_view(), name='mugs_create'),
    path('mugs/<int:pk>/update/', views.MugUpdate.as_view(), name='mugs_update'),
    path('mugs/<int:pk>/delete/', views.MugDelete.as_view(), name='mugs_delete'),
    path('mugs/<int:mug_id>/add_drink/', views.add_drink, name='add_drink'),
    path("mugs/<int:mug_id>/delete_drink/<int:drink_id>", views.delete_drink, name="delete_drink")
]