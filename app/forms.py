from django import forms
from .models import Contact

class Contact_form(forms.ModelForm):

    class Meta:

        model=Contact

        fields=["choose_service","name","phone","message"]


        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name', }),

                'phone': forms.TextInput(attrs={'class': 'form-control ','placeholder': 'Your Phone',}),
                
                'message': forms.Textarea(attrs={'class': 'form-control ','placeholder': 'Your Message...','rows': 3,}),

                'choose_service':forms.Select(attrs={"class":"form-select ","placeholder":"choose service"})
            }