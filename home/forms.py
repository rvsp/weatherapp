from django import forms

class SearchPlace(forms.Form):
	
	place = forms.CharField(
            label='', 
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "Find your Loaction...",
                        "class": "locate"
                        }
                )
            )