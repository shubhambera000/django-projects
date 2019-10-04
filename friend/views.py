from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect;
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def index(request):
    return render(request, 'base.html')


def detail(request):
    return render(request, 'index.html')


class LoginView(TemplateView):
    template_name = "registration/login.html"
