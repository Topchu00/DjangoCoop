from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from .forms import *

def home(request):
    up_gallery = UpImages.objects.all()
    form = formContact()
    context = {'up_gallery': up_gallery, 'form': form}

    if request.method == "POST":
        form = formContact(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data["name"]
            your_email = form.cleaned_data["email"]
            your_phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            ListForm = FormsList.objects.all()
            FormsList.objects.create(
                name=your_name,
                phone=your_phone,
                email=your_email,
                message=message
            )

            return HttpResponseRedirect("/")
    else:
        return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def brand(request):
    up_gallery = UpImages.objects.all()
    context = {'up_gallery': up_gallery}
    return render(request, 'brand.html', context)


def special(request):
    return render(request, 'special.html')


def contact(request):
    if request.method == "POST":
        form = formContact(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data["name"]
            your_email = form.cleaned_data["email"]
            your_phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            ListForm = FormsList.objects.all()
            FormsList.objects.create(
                name=your_name,
                phone=your_phone,
                email=your_email,
                message=message
            )

            return HttpResponseRedirect("/")
    else:
        form = formContact()
        return render(request, "contact.html", {"form":form})