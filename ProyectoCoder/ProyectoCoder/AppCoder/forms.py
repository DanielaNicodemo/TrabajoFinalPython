from django import forms

class ContactoFormulario(forms.Form):
    nombre= forms.CharField()
    mail= forms.CharField(required=True)
    telefono= forms.IntegerField()
    mensaje= forms.CharField()