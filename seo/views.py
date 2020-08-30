from django.views import generic

from seo.models import RobotsTxt, RobotsHost


class RobotsTxtView(generic.ListView):
    """ View for getting robots.txt file """

    template_name = "app/seo/robots.html"
    queryset = RobotsTxt.objects.filter(is_active=True)
    context_object_name = 'robots'

    def get_context_data(self, **kwargs):
        context = super(RobotsTxtView, self).get_context_data(**kwargs)
        context['host'] = RobotsHost.objects.first()
        return context
