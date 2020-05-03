from seo.models import GlobalSeo
from vcard.models import SiteConfig


def global_settings_context(request):
    context = {
        'GLOBAL_SEO': GlobalSeo.objects.first(),
        'SITE_SETTINGS': SiteConfig.objects.first()
    }

    return context
