from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
from django.views import View
# Create your views here.
class contact(View):
  def get(self, request):
    cf = contact_Form
    return render(request, 'contact/contact.html', {'cf': cf})

  def Subscriber(request):
      a = Subscriber()
      return render(request, 'contact/contact.html', {'f': a})

  def Submit(request):
      if request.method == 'POST':
          g = Subscriber(request.POST)
          if g.is_valid():
              g.save()
              return render(request, 'contact/contact.html')
          else:
              return render(request, 'contact/contact.html')

