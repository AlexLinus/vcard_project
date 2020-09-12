import json

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views import generic

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .models import Gallery, Skills
from .forms import ContactForm
# Create your views here.


class HomePageView(generic.TemplateView):
    """ View for getting Home page """
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['skills'] = Skills.objects.filter(is_active=True)
        return context


class PortfolioView(generic.ListView):
    """ View for getting Portfolio items (projects) """
    queryset = Gallery.objects.filter(is_active=True)
    template_name = 'app/portfolio.html'
    context_object_name = 'portfolio_items'


class ProjectDetailView(generic.DetailView):
    """ View for getting Project detail """
    model = Gallery
    template_name = 'app/project_detail.html'


class ContactPageView(generic.TemplateView):
    """ View for getting Contact Page """
    template_name = 'app/contact_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context


def send_message(request):
    """ function for ajax view of sending email to site admin """
    full_form = ContactForm(request.POST)
    if request.is_ajax():
        if full_form.is_valid():
            subject = f'Письмо с сайта vcard, от { full_form.cleaned_data["your_name"]} { full_form.cleaned_data["your_email"]}'
            email_from = settings.DEFAULT_FROM_EMAIL
            message = f'от { full_form.cleaned_data["your_email"]}  \r\n {full_form.cleaned_data["message"]}'
            recipient_list = [settings.DEFAULT_EMAIL_TO]
            try:
                send_mail(subject, message, email_from, recipient_list)
            except Exception as E:
                print(E)
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