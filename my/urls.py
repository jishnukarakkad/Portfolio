# my/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('certificates/',views.certificates,name='certificates'),
    path('skills/',views.skills,name='skills'),
    path('contact/', views.contact, name='contact'),
    
]
