from django import forms
from .models import ContactMessage
from django.core.validators import EmailValidator

class ContactForm(forms.ModelForm):
    class Meta:
            model = ContactMessage
                    fields = ('name', 'email', 'message')
                            widgets = {
                                        'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
                                                    'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
                                                                'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
                                                                        }

                                                                            def clean_email(self):
                                                                                    email = self.cleaned_data.get('email')
                                                                                            validator = EmailValidator()
                                                                                                    try:
                                                                                                                validator(email)
                                                                                                                        except forms.ValidationError:
                                                                                                                                    raise forms.ValidationError("Invalid email address.")
                                                                                                                                            return email

                                                                                                                                                def clean_message(self):
                                                                                                                                                        message = self.cleaned_data.get('message')
                                                                                                                                                                if len(message) < 10:
                                                                                                                                                                            raise forms.ValidationError("Message should be at least 10 characters long.")
                                                                                                                                                                                    return message