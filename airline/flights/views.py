from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request): 
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id): 
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all() # Exclude passengers that satisfy a specific query 
    })

def book(request, flight_id): # Implementing the book view
    if request.method == "POST": 
        flight = Flight.objects.get(pk=flight_id) # To get a particular flight with the flight ID
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"])) # This means that the data about which passenger ID we want to register on this flight is going to be passed in via a form with an input field whose name is passenger
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id))) # Redirects the user to the flights page 
