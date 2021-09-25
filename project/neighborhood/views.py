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
