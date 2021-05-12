from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, room_choices, province_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    top_three = Realtor.objects.all().filter(is_top_three=True)
    context = {
        'listings': listings,
        'top_three' : top_three,
        'price_choices' : price_choices,
        'province_choices' : province_choices,
        'room_choices' : room_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all Realtors 
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html', context);