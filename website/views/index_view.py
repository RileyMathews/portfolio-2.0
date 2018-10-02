from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ 
        Class to generate the index view for the web page
    """

    template_name = "website/index.html"

