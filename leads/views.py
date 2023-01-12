from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm

# Create your views here.
def lead_list(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"leads/lead_list.html", context)



def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request,"leads/lead_detail.html", context)


def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            # the form doesn't include an agent -> have to add it yourself!
            agent = Agent.objects.first() # -> first row in the table
            Lead.objects.create( #creates a new lead in the DB
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")
    context = {
        "form": form #create an instance of the form; can validate the info
    }
    return render(request, "leads/lead_create.html", context)