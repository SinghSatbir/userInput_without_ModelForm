from django.http import HttpResponse
from django.template import loader

from app_users.models import User
from app_users.forms import Aform


def index(request):
    template = loader.get_template('users_app/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def user_view(request):
    template = loader.get_template('users_app/users.html')
    context = {
        'users_set': User.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def form_view(request):
    template = loader.get_template('users_app/forms_page.html')
    form_object = Aform()
    if request.method == 'POST':
        form_object = Aform(request.POST)
        if form_object.is_valid():
            entered_name = form_object.cleaned_data['first_name']
            entered_email = form_object.cleaned_data['email']
            entered_lname = form_object.cleaned_data['last_name']
            User.objects.get_or_create(first_name=entered_name, last_name=entered_lname, email=entered_email)

    context = {

        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))
