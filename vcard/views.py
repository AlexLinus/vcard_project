from django.shortcuts import render, get_object_or_404
from .models import Gallery
# Create your views here.

def home_view(request):
    return render(request, 'vcard/home.html')

def portfolio_detail(request):
    portfolio_items = Gallery.objects.filter(is_active=True)
    return render(request, 'vcard/portfolio.html', context={'portfolio_items': portfolio_items})

def project_detail(request, project_slug):
    project = get_object_or_404(Gallery, slug=project_slug)
    return render(request, 'vcard/project_detail.html', context={'project': project})

def contact_detail(request):
    return render(request,'vcard/contact_detail.html')