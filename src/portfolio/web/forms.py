from django.forms import ModelForm
from django import forms
from web.models import Contact


class ContactForm(ModelForm) :
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : forms.widgets.EmailInput(attrs = {"placeholder" : "Enter Email "}),
            "name" : forms.widgets.TextInput(attrs = {"placeholder" : "Enter Name "}),
            "phone" : forms.widgets.TextInput(attrs = {"placeholder" : "Enter Phone Number "}),
            "message" : forms.widgets.Textarea(attrs = {"placeholder" : "Enter your message here.........."}),

        }