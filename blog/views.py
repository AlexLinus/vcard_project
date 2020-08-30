import json

from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponse

from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


from .models import Posts, Category
from .forms import CommentForm

# Create your views here.


class BlogPageView(generic.ListView):
    """ View for Blog Page (list of posts) """
    queryset = Posts.objects.filter(is_active=True)
    paginate_by = 5
    template_name = 'app/blog.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    """ View for getting Post Detail """
    queryset = Posts.objects.filter(is_active=True)
    template_name = 'app/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # если не сработает попробовать через self.get_object().id
        if f'post_views_{self.object.id}' not in self.request.session:
            self.request.session[f'post_views_{self.object.id}'] = self.object.id
            self.object.views += 1
            self.object.save()

        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        context['related_posts'] = Posts.objects.filter(is_active=True).exclude(id=self.object.id)[:3]
        context['comment_form'] = CommentForm()
        return context


class CategoryDetailView(generic.DetailView):
    """ View for getting Category Detail """
    template_name = 'app/category_detail.html'
    model = Category
    context_object_name = 'category'


def add_comment(request, slug):
    """ function view for adding comment via ajax """
    post = get_object_or_404(Posts, slug=slug)
    full_form = CommentForm(request.POST)
    if request.is_ajax():
        if full_form.is_valid():
            new_comment = full_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            to_json_response = dict()
            to_json_response['status'] = 1
            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
            to_json_response['new_comment_author_name'] = new_comment.author_name
            to_json_response['new_comment_pub_date'] = str(new_comment.pub_date)
            to_json_response['new_comment_body'] = new_comment.comment_body
            to_json_response['new_comment_id'] = new_comment.id
        else:
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = full_form.errors
            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

    return HttpResponse(json.dumps(to_json_response), content_type='application/json')
