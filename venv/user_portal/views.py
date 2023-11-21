from django.views.generic.edit import CreateView
from .forms import RegistroForm
from django.urls import reverse_lazy

# Create your views here.
class Registro(CreateView):
  template_name = 'cadastro.html'
  form_class = RegistroForm
  success_url = reverse_lazy('login')