from django.shortcuts import render,redirect
from django.views.generic import View
from . models import Services,Contact
from .forms import Contact_form
from django.contrib import messages

# Create your views here.
def Home_view(request):
    qs=Services.objects.all()
    if request.method=="POST":
        form=Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request,"Try again")
    else:
        form=Contact_form()
    return render(request,"home.html",{"data":qs,"form":form})

