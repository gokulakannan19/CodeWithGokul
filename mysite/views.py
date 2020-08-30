from django.shortcuts import render
from .models import Projects, Services, Queries

# Create your views here.


def homepage(request):
    return render(request, "mysite/homepage.html")


def about(request):
    return render(request, "mysite/about.html")


def services(request):
    services = Services.objects.all()
    context = {
        "services": services
    }
    return render(request, "mysite/services.html", context)


def projects(request):
    projects = Projects.objects.all()
    # print(projects)
    # for project in projects:
    #     print(project.project_name)
    context = {
        "projects": projects
    }

    return render(request, "mysite/projects.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        print(name)
        print(email)
        print(message)

        Queries.objects.create(
            customer_name=name, customer_email=email, customer_query=message)

    return render(request, "mysite/contact.html")
