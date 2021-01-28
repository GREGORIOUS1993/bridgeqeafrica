from django import forms

class contactformemail(forms.Form):
	subject 	= forms.CharField(required=True, widget=forms.TextInput(attrs={'size': '40'}))
	email		= forms.EmailField(required=True, widget=forms.TextInput(attrs={'size': '40'}))
	message		= forms.CharField(widget=forms.Textarea,required=True)