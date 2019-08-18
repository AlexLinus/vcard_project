"""vcard app urls
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('contacts/', views.contact_detail, name='contact_url'),
    path('contacts/send_message/', views.send_message, name='send_message_url'),
    path('portfolio/', views.portfolio_detail, name='portfolio_url'),
    path('portfolio/<str:project_slug>/', views.project_detail, name='project_url'),
]
