from django.shortcuts import render,redirect
from django.urls import reverse
from cars.forms import ReviewForm

# Create your views here.

def review_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))
        else:
            return render(request, "cars/review_page.html", {"form": form}) 
            
    else:
        form = ReviewForm()
        return render(request, "cars/review_page.html", {"form": form})

def thank_you_view(request):
    return render(request, "cars/thank_you_page.html")
