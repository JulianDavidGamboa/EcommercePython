from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title": "Home page",
        "content": "Welcome to the home page"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the about page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    
    return render(request, "auth/login.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})