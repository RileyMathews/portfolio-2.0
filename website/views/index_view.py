from django.views.generic import TemplateView
from website.models import Technology, Project
from django.shortcuts import render


def index_view(request):
    """function to render the index view of the website
    
    Arguments:
        request {http request} -- the full http request object
    
    Returns:
        render -- the django render shortcut
    """
    print("loading index")
    technologies = Technology.objects.all()
    projects = Project.objects.all()

    data = {"technologies": technologies, "projects": projects}
    return render(request, "website/index.html", {"data": data})

