from django.shortcuts import render
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
  form_action = reverse('contact:create')
  if request.method == 'POST':
    context = {
      'form': ContactForm(request.POST)
    }
  
    return render(
      request,
      'contact/create.html',
      context 
    )
  context = {
    'form': ContactForm()
  }
  
  return render(
    request,
    'contact/create.html',
    context 
  )