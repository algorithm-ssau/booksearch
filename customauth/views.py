from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@never_cache
def to_read(request):
    reading_list = request.user.to_read.all()
    return render(request, 'customauth/to_read.html', {'reading_list' : reading_list})
