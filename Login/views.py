from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,render_to_response
from .forms import DetailsForm
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url="login/")
def page1(request):
    return render(request,"Home.html")

def Home(request):
    return render(request,"Start.html")


def Detail(request):
    form = DetailsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, "Start.html", {})

    context = {
        "form": form,

    }
    return render(request, 'FormFill.html', context)


def register_user(request):
    form2=MyRegistrationForm(request.POST or None)
    if form2.is_valid():
            form2.save()
            return render(request,'start.html')
    dict={
        "form2":form2
    }
    return render(request, 'Signup.html', dict)

