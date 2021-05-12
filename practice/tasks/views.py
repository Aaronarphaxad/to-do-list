from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="priority",min_value=1, max_value=10)

def index(request):
    # if there is no list called tasks in session, create an empty list called tasks
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {'tasks': request.session["tasks"]})

def add(request):
    if request.method == "POST":
        # get data from form
        form = NewTaskForm(request.POST)
        # validate
        if form.is_valid():
            # variables from the class
            task = form.cleaned_data["task"]
            # add task to the tasks in the session
            request.session["tasks"] += [task]
            # on add, redirect to index page
            return HttpResponseRedirect(reverse("index"))
        else:
            # send back existing form if form is not valid
            return render(request, "tasks/add.html", {
            "form": form
            })
    # return empty form if request is get
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })