from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.

def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save() #sending the final post request
            return redirect('home.html') #check to see if this works

    context = {'form':form}


    return render(request, 'account/registration/register.html', context=context)