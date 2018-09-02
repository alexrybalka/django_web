from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('vehiclepart-search/', views.search_vehicleparts,
         name='vehiclepart-search-result'),
    path('section-search/', views.search_sections,
         name='section-search-result'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('add_section/', views.add_section, name='add-new-section'),
    path('add_vehiclepart/', views.add_vehiclepart, name='add-new-vehiclepart'),
    path('top-priced/', views.top_priced, name='top-priced'),
    path('sections/<str:section_name>/', views.section, name='section'),
    path('section/edit/<int:section_id>', views.edit_section,
         name='edit-section'),
    path('vehiclepart/edit/<int:vehiclepart_id>', views.edit_vehiclepart,
         name='edit-vehiclepart'),
    path('sections/', views.sections, name='sections'),
]
