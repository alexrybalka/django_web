from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import VehiclePart, Section
from .forms import SectionForm, VehiclePartForm


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            messages.add_message(request, messages.INFO,
                                 f"Congrats! {new_user.username} was logined successfully")
            return HttpResponseRedirect('/')
    else:
        return render_to_response("registration/register.html", {
        'form': form
    })

def auth(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        if form.is_valid():
            messages.add_message(request, messages.INFO,
                                 f"Congrats! {inst.username} was logined successfully")
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'web_car/auth.html', {
        'form': form
    })


def index(request):
    return render(request, 'web_car/index.html', {
        'amount_vehiclepart': VehiclePart.objects.all().count(),
    })


def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            inst = form.save()
            messages.add_message(request, messages.INFO,
                                 f"Section {inst.name} was created successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = SectionForm()
    return render(request, 'web_car/add_section.html', {
        'form': form
    })


def add_vehiclepart(request):
    if request.method == 'POST':
        form = VehiclePartForm(request.POST)
        if form.is_valid():
            inst = form.save()
            messages.add_message(request,
                                 messages.INFO,
                                 f"Vehicle Part {inst.name} was created successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = VehiclePartForm()
    return render(request, 'web_car/add_vehiclepart.html', {
        'form': form
    })


def sections(request):
    return render(request, 'web_car/sections.html', {
        'section_list': Section.objects.all(),
    })


def section(request, section_name):
    vehiclepart_list = VehiclePart.objects.filter(section__name=section_name)
    return render(request, 'web_car/section.html', {
        'section_name': section_name,
        'vehiclepart_list': vehiclepart_list,
    })


def top_priced(request):
    priciest_vehiclepart_list = VehiclePart.objects.order_by('-price')[:5]
    return render(request, 'web_car/top-priced.html', {
        'priciest_vehiclepart_list': priciest_vehiclepart_list,
    })
