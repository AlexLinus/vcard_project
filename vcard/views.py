from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery, Skills
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json
# Create your views here.


def home_view(request):

    context = {
        'skills': Skills.objects.filter(is_active=True)
    }

    return render(request, 'app/home.html', context)


def portfolio_detail(request):
    portfolio_items = Gallery.objects.filter(is_active=True)
    return render(request, 'app/portfolio.html', context={'portfolio_items': portfolio_items})


def project_detail(request, project_slug):
    project = get_object_or_404(Gallery, slug=project_slug)
    return render(request, 'app/project_detail.html', context={'project': project})


def contact_detail(request):
    form = ContactForm()
    return render(request, 'app/contact_detail.html', context={'form': form})


def send_message(request):
    full_form = ContactForm(request.POST)
    if request.is_ajax():
        if full_form.is_valid():
            subject = f'Письмо с сайта vcard, от { full_form.cleaned_data["your_name"]} { full_form.cleaned_data["your_email"]}'
            email_from = settings.EMAIL_HOST_USER
            message = f'от { full_form.cleaned_data["your_email"]}  \r\n {full_form.cleaned_data["message"]}'
            recipient_list = ['kelevra141993@gmail.com',]
            try:
                send_mail(subject, message, email_from, recipient_list)
            except Exception as e:
                pass
            to_json_response = dict()
            to_json_response['status'] = 1
            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

        else:
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = full_form.errors

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
        return HttpResponse(json.dumps(to_json_response), content_type='application/json')

