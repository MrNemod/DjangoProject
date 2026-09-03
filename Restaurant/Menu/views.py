from django.shortcuts import render
from Menu import views

# Create your views here.
def menu(request):
    return render(request, 'menu.html')
