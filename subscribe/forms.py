from django import forms

class Subscribe(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Title = forms.CharField()
    Body = forms.CharField()

    def __str__(self):
        return self.Email