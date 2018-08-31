from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('results/', views.search, name='vehicleparts-search'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('add_section/', views.add_section, name='add-new-section'),
    path('add_vehiclepart/', views.add_vehiclepart, name='add-new-vehiclepart'),
    path('top-priced/', views.top_priced, name='top-priced'),
    path('sections/<str:section_name>/', views.section, name='section'),
    path('section/edit/<int:section_id>', views.edit_section,
         name='edit-section'),
    path('vehiclepart/edit/<int:vehiclepart_id>', views.edit_vehiclepart,
         name='edit_vehiclepart'),
    path('sections/', views.sections, name='sections'),
]
