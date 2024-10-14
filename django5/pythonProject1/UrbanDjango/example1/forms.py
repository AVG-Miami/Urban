from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Выше имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    subscribe = forms.CharField(required=False, label='Подписатьс на рассылку ')
