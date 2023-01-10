from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Global tasks veriables
tasks = []


class NewForm(forms.Form):
    task = forms.CharField(label='New Task')
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'tasks/index.html',{
        "tasks" : request.session['tasks']
    })

def add(request):
    # The user submit the form
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            # take the data from the from
            task = form.cleaned_data['task']
            # add task to session
            request.session['tasks'] += [task]
            # redirect
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })
    # The user made get request for form
    else:    
        return render(request, 'tasks/add.html',{
            "form": NewForm()
        })
