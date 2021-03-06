from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileChange(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('index')
    template_name = 'profile_change.html'

class ProfileDelete(generic.DeleteView):
    model = CustomUser
    success_url = reverse_lazy('index')
    template_name = 'profile_delete.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(self.success_url)
        else:
            return super(ProfileDelete, self).post(request, *args, **kwargs)

@never_cache
def to_read(request):
    reading_list = request.user.to_read.all()
    return render(request, 'customauth/to_read.html', {'reading_list' : reading_list})
