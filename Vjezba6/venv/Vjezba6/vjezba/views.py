from django.shortcuts import render
from django.http import HttpResponse
# from .forms import BookForm
from .models import USERS, PROJECTION, TICKET
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def show_projections(request):
    if request.method == 'GET':
        all_projections = PROJECTION.objects.all()
        return render(request, 'projections.html', {'projections':all_projections})
    elif request.method == 'POST':
        quantity = request.POST.get("quantity")
        return HttpResponse(quantity)

def register(request):
    if request.method == 'GET':
        userForm = UserCreationForm()
        return render(request, 'register.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('show_projections')
        else:
            return render(request, 'register.html', {'form':userForm})
    else:
        return HttpResonseNotAllowed()
