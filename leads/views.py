from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic # -> better
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomerUserCreation
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here -> how to handle web requests

# CRUD - create, retrieve, update, delete + list (lead_list) -> every page fall sunder one of these



class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
        # queryset = Lead.objects.all() # -> passed into context
    form_class = CustomerUserCreation # custom on ethat uses our own model

    # WHat to do when the form is submitted successfully
    def get_success_url(self) -> str:
        return reverse("login") # "/leads" is manual -> this better


# Can also use class based views
class LandingPageView(LoginRequiredMixin, generic.TemplateView): # inherit from django class based views
    template_name = "landing.html" #required for TemplateView

def landing_page(request):
    return render(request, "landing.html")


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all() # -> passed into context
    context_object_name = "leads" #specify the var in the template

# def lead_list(request):
#     # return HttpResponse("Hello world")
#     leads = Lead.objects.all()
#     context = {
#         "object_list": leads
#     }
#     return render(request,"leads/lead_list.html", context)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all() # -> passed into context
    context_object_name = "lead" #specify the var in the template

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request,"leads/lead_detail.html", context)


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    # queryset = Lead.objects.all() # -> passed into context
    form_class = LeadModelForm

    # WHat to do when the form is submitted successfully
    def get_success_url(self) -> str:
        return reverse("leads:lead-list") # "/leads" is manual -> this better


    def form_valid(self, form):
        # TODO: send email
        send_mail(
            subject="A lead has been created", 
            message="Go to the site to see the new lead",
            from_email="tzver@outlook.com",
            recipient_list=["tzver@outlook.com"]

        )
        return super(LeadCreateView, self).form_valid(form) #continue what it was going to do in form_valid -> only add sth in between processes

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form #create an instance of the form; can validate the info
#     }
#     return render(request, "leads/lead_create.html", context)




class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all() # -> passed into context
    form_class = LeadModelForm

    # WHat to do when the form is submitted successfully
    def get_success_url(self) -> str:
        return reverse("leads:lead-list") # "/leads" is manual -> this better

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead) #grab an instance and update it!
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request,"leads/lead_update.html", context)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all() # -> passed into context

    # WHat to do when the form is submitted successfully
    def get_success_url(self) -> str:
        return reverse("leads:lead-list") # "/leads" is manual -> this better


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")


########### OLD CODE ############


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save() #commit the data to a DB
#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request,"leads/lead_update.html", context)




# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             # the form doesn't include an agent -> have to add it yourself!
#             agent = Agent.objects.first() # -> first row in the table
#             Lead.objects.create( #creates a new lead in the DB
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             return redirect("/leads")
#     context = {
#         "form": form #create an instance of the form; can validate the info
#     }
#     return render(request, "leads/lead_create.html", context)