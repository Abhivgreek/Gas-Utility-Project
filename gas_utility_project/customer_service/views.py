from django.shortcuts import render
from .models import ServiceRequest
from django.http import HttpResponse

def customer_request_list(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'customer_service/customer_request_list.html', {'service_requests': service_requests})

def support_rep_dashboard(request):
    # Include logic to list assigned requests, etc.
    return render(request, 'customer_service/support_rep_dashboard.html', {})

def index(request):
    return HttpResponse("Customer Service App Home")

def home(request):
    return HttpResponse("Welcome to the Gas Utility Management System!")