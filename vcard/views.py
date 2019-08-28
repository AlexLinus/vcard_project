from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings
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
    form = ContactForm()
    return render(request,'vcard/contact_detail.html', context={'form': form})

def send_message(request):
    if request.method == "POST":
        full_form = ContactForm(request.POST)
        if full_form.is_valid():
            subject = f'Письмо с сайта vcard, от { full_form.cleaned_data["your_name"]}'
            email_from = settings.EMAIL_HOST_USER
            message = full_form.cleaned_data['message']
            recipient_list = ['kelevra141993@gmail.com',]
            try:
                send_mail(subject, message, email_from, recipient_list)
                print('Сработало TRY')
            except Exception as e:
                print(f'Ошибка: {e}')
        return redirect('contact_url')

