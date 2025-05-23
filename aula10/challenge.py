# Challenge Session 10: Django Security Measures
# Problem: Secure a Django application by implementing comprehensive security measures: CSRF protection, secure session management, and input validation.
# Hint: Use Django’s built-in security middleware and forms.

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django import forms

@csrf_protect
def my_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # process data
            pass
    else:
        form = MyForm()
    return render(request, "my_template.html", {"form": form})



class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name
