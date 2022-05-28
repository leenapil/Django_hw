from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def school(request):
    return render(request, 'school.html')

def favorite(request):
    return render(request, 'favorite.html')

def pratice(request):
    return render(request, 'pratice.html')

def table(request):
    return render(request, 'table.html')

def home(request):
    return render(request, 'home.html')




