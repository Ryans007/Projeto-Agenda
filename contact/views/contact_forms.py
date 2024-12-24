from django.shortcuts import render
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
  form_action = reverse('contact:create')
  if request.method == 'POST':
    context = {
      'form': ContactForm(request.POST),
      'form_action': form_action,
    }
  
    return render(
      request,
      'contact/create.html',
      context 
    )
  context = {
    'form': ContactForm(),
    'form_action': form_action,
  }
  
  return render(
    request,
    'contact/create.html',
    context 
  )