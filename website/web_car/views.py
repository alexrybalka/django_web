from django.contrib import messages
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.paginator import Paginator

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
                                 f"Congrats! {new_user.username} was registered successfully")
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
            name__contain=request.GET['search'])
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
    return render(request, 'web_car/section.html', {
        'section_name': section_name,
        'vehiclepart_list': vehiclepart_list,
    })


def top_priced(request):
    priciest_vehiclepart_list = VehiclePart.objects.order_by('-price')[:5]
    return render(request, 'web_car/top-priced.html', {
        'priciest_vehiclepart_list': priciest_vehiclepart_list,
    })
