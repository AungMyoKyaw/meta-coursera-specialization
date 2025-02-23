from django.shortcuts import render

def home(request):
    return render(request, "home.html")  # Now points to the global templates folder
