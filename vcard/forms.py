from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    captcha = CaptchaField()
    your_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'site-input', 'placeholder': 'Ваше имя'}), max_length=100)
    your_email = forms.EmailField(label='Ваш e-mail', required=True, widget=forms.TextInput(attrs={'class': 'site-input', 'placeholder': 'Ваш e-mail'}))
    message = forms.CharField(label='Сообщение', max_length='300', widget=forms.Textarea(attrs={'class': 'site-area', 'placeholder': 'Сообщение'}))



