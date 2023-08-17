from django.shortcuts import render
from django.views.generic import DetailView,TemplateView


from .models import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"
    context_object_name = "project"

class AboutView(TemplateView):
    template_name = 'about.html'


def game_dev_project_list(request):
    projects = Project.objects.all().filter(project_type__icontains="game-dev")
    return render(request,"game_dev_projects.html",{'projects':projects})


def web_dev_project_list(request):
    projects = Project.objects.all().filter(project_type__icontains="web-dev")
    return render(request,"web_dev_projects.html",{'projects':projects})