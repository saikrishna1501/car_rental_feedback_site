from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=100)
#     last_name = forms.CharField(label="Last Name", max_length=100)
#     email = forms.EmailField(label="Email Id", widget=forms.EmailInput(attrs={'class': 'border-5px'}))
#     review = forms.CharField(label="Review", max_length=200, widget=forms.Textarea(attrs={'class': 'border-5px', 'cols': '40', 'rows': '5'}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = "__all__" #you can use this if you want to pass all fields instead of passing all to the list
        fields = ['first_name', 'last_name', 'reviews']
        labels = {
            'first_name' : "Enter Your First Name",
            'last_name': "Enter Your Last Name",
            'reviews': 'stars'
        }
        #if you want to customize the error messages for fields, you can do the following. 
        #The error keys for a particular type of field needs to be looked up from documentation
        #for example for IntegerField we have max_value, min_value, required etc
        error_messages = {
            "reviews": {
                "max_value": "Max value is 5",
                "min_value": "Min value is 1"
            }
        }
    