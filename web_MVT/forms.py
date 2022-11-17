from django import forms

class categoriForm (forms.Form):
    name = forms.CharField()
    description = forms.CharField()

class productForm(forms.Form):
    code = forms.IntegerField()
    name = forms.CharField()
    description = forms.CharField()
    category = forms.CharField()
    price = forms.FloatField()
    
class registerForm(forms.Form):
    firtname = forms.CharField()
    lastname= forms.CharField()
    phone = forms.IntegerField()
    email= forms.EmailField()
    password = forms.CharField()