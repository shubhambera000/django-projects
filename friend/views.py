from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.decorators import login_required
from .forms import AddressForm, CrispyAddressForm, CustomFieldForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm


class AddressFormView(FormView):
    form_class = AddressForm


class CrispyAddressFormView(FormView):
    form_class = CrispyAddressForm
    template_name = 'jai.html'


class CustomFieldFormView(FormView):
    form_class = CustomFieldForm
    template_name = 'jai.html'


def register_view(request):
    next = request.GET.get('next')
    form = CustomFieldForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('home/')
    context = {
        'form': form,
    }
    return render(request, "jai.html", context)


@login_required
def home(request):
    return render(request, "base.html", {})


def login_view(request):
    next = request.GET.get('next')
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home/')
    context = {
        'form': form,
    }
    return render(request, "index.html", context)
