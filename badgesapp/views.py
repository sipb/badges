from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def badges(request):
    return render(request, 'badges.html')