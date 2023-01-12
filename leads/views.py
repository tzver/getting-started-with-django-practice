from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def home_page(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"second_page.html", context)