import json 

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Skill
from web.forms import ContactForm


def index(request):
    skills  = Skill.objects.filter(skill_type= "frontend")
    backend  = Skill.objects.filter(skill_type= "backend")
    devops  = Skill.objects.filter(skill_type= "devops")
    api  = Skill.objects.filter(skill_type= "API_development")
    form = ContactForm()

    context = {
        "skills" : skills,
        "backend" : backend,
        "devops" : devops,
        "api" : api,
        "title" : "Portfolio |",
        "form" : form
    }
    return render(request, "index.html" ,context = context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        request_data = {
            "title": "successfully done",
            "status": "success",
            "message": " Message send Successsfully"
            }
    else:
        request_data = {
            "title": "Something Error",
            "status": "error",
            "message": "Please Try after sometimes..!"
            }

    return HttpResponse (json.dumps(request_data), content_type = "application/javascript")
