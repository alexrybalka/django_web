from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_section/', views.add_section, name='add-new-section'),
    path('add_vehiclepart/', views.add_vehiclepart, name='add-new-vehiclepart'),
    path('top-priced/', views.top_priced, name='top-priced'),
    path('sections/<str:section_name>/', views.section, name='section'),
    path('sections/', views.sections, name='sections'),
]
