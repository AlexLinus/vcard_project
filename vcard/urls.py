"""vcard app urls
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_url'),
    path('contacts/', views.ContactPageView.as_view(), name='contact_url'),
    path('contacts/send_message/', views.send_message, name='send_message_url'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio_url'),
    path('portfolio/<str:project_slug>/', views.ProjectDetailView.as_view(), name='project_url'),
]
