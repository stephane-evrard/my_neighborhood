from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    date = dt.date.today()
    # business = Business.get_allbusiness()
    all_neighborhoods = Neighborhood.get_neighborhoods()
    
    
    if 'neighborhood' in request.GET and request.GET["neighborhood"]:
        neighborhoods = request.GET.get("neighborhood")
        searched_neighborhood = Business.get_by_neighborhood(neighborhoods)
        all_posts = Posts.get_by_neighborhood(neighborhoods)
        message = f"{neighborhoods}"
        all_neighborhoods = Neighborhood.get_neighborhoods()        
        
        return render(request, 'index.html', {"message":message,"location": searched_neighborhood,
                                               "all_neighborhoods":all_neighborhoods, "all_posts":all_posts})

    else:
        message = "No Neighborhood Found!"

    return render(request, 'index.html', {"date": date, "all_neighborhoods":all_neighborhoods,})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_businesses(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"businesses": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def get_business(request, id):

    try:
        project = Business.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
    
    
    return render(request, "projects.html", {"project":project})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Admin = current_user
            project.admin_profile = profile
            project.save()
        return redirect('index')

    else:
        form = NewBusinessForm()
    return render(request, 'new-business.html', {"form": form})

