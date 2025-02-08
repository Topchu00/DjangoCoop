from django import forms

class formContact(forms.Form):
    name = forms.CharField(max_length=40, label="Ваше имя", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя", "type": "text"}))
    email = forms.EmailField(label="Ваша почта", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ваша почта", "type": "text"}))
    phone = forms.CharField(max_length=20, label="Ваш номер", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваш номер", "type": "text"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea", "placeholder": "Ваше сообщение", "type": "text"}), label='Ваше сообщение')