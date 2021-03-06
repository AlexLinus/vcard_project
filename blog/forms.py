from django import forms
from .models import Comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments
        exclude = ['pub_date', 'parrent_comment', 'pub_date', 'post']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'site-input', 'placeholder': 'Имя'}),
            'author_email': forms.EmailInput(attrs={'class': 'site-input', 'placeholder': 'E-mail'}),
            'comment_body': forms.Textarea(attrs={'class': 'site-area', 'placeholder': 'Текст комментария'}),
        }