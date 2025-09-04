from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutUsView(TemplateView):
    template_name = "core/about_us.html"
