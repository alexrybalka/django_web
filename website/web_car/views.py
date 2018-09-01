from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView

from .models import VehiclePart, Section
from .forms import SectionForm, VehiclePartForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()
            messages.add_message(request, messages.INFO,
                                 f"Congrats! {inst.username} was registered successfully")
            return HttpResponseRedirect("/")
        else:
            return render(request, "registration/register.html", {
                'form': form
            })
    else:
        return render(request, "registration/register.html", {
            'form': UserCreationForm()
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
            inst.user = request.user
            inst.save()
            messages.add_message(request, messages.INFO,
                                 f"Section {inst.name} was created successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = SectionForm()
    return render(request, 'web_car/add_section.html', {
        'form': form
    })


def edit_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    if request.user != section.user:
        return HttpResponseNotFound()
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()
            messages.add_message(request, messages.INFO,
                                 f"Section {inst.name} was edited successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = SectionForm(instance=section)
    return render(request, 'web_car/add_section.html', {
        'form': form
    })


def edit_vehiclepart(request, vehiclepart_id):
    vehiclepart = get_object_or_404(VehiclePart, id=vehiclepart_id)
    if request.user != vehiclepart.user:
        return HttpResponseNotFound()
    if request.method == 'POST':
        form = VehiclePartForm(request.POST, instance=vehiclepart)
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()
            messages.add_message(request,
                                 messages.INFO,
                                 f"Vehicle Part {inst.name} was edited successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = VehiclePartForm(instance=vehiclepart)
    return render(request, 'web_car/add_vehiclepart.html', {
        'form': form
    })


def add_vehiclepart(request):
    if request.method == 'POST':
        form = VehiclePartForm(request.POST)
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()
            messages.add_message(request,
                                 messages.INFO,
                                 f"Vehicle Part {inst.name} was created successfully")
            return HttpResponseRedirect('/sections/')
    else:
        form = VehiclePartForm()
    return render(request, 'web_car/add_vehiclepart.html', {
        'form': form
    })


def search(request):
    if 'search' in request.GET:
        vehicleparts = VehiclePart.objects.filter(
            name__contains=request.GET['search'])
    return render(request, 'web_car/results.html', {
        'vehicleparts': vehicleparts,
    })


def sections(request):
    p = Paginator(object_list=Section.objects.all(), per_page=5)
    return render(request, 'web_car/sections.html', {
        'section_list': p.page(request.GET.get('page', 1)),
        'paginator': p,
    })


def section(request, section_name):
    vehiclepart_list = VehiclePart.objects.filter(
        section__name=section_name).order_by('-price')
    p = Paginator(vehiclepart_list, per_page=2)
    return render(request, 'web_car/section.html', {
        'section_name': section_name,
        'paginator': p,
        'vehiclepart_list': p.page(request.GET.get('page', 1)),
    })


def top_priced(request):
    priciest_vehiclepart_list = VehiclePart.objects.order_by('-price')[:5]
    return render(request, 'web_car/top-priced.html', {
        'priciest_vehiclepart_list': priciest_vehiclepart_list,
    })
