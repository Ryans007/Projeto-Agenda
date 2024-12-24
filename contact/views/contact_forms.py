from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
  form_action = reverse('contact:create')
  if request.method == 'POST':
      form = ContactForm(request.POST)
      context = {
        'form': form,
        'form_action': form_action,
      }
      
      if form.is_valid():
        form.save()
        return redirect('contact:create')
     
    
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