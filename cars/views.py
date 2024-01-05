from django.shortcuts import render

# Create your views here.

def review_view(request):
    return render(request, "cars/review_page.html")

def thank_you_view(request):
    return render(request, "cars/thank_you_page.html")
