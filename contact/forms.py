from django import forms
from django.core.exceptions import ValidationError
from . import models 


class ContactForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
        
      self.fields['first_name'].widget.attrs.update({
          'class':'classe-a classe-b',
          'placeholder': 'Escreva aqui'
  })
  class Meta:
    model = models.Contact
    fields = (
      'first_name', 'last_name', 'phone',
    )
    # widgets = {
    #   'first_name': forms.TextInput(
    #     attrs={
    #       'class':'classe-a classe-b',
    #       'placeholder': 'Escreva aqui'
    #     }
    #   )
    # }
