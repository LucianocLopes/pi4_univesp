from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreateForm, ProfileUpdateForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'accounts/registration/registro.html'
    
    def get_success_url(self):
        # Redireciona para a URL de atualização (edição) do objeto recém-criado
        return reverse_lazy('profile_edit', kwargs={'pk': self.object.pk})

    
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'accounts/registration/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})
    
def profile_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/registration/profile_detail.html', {'pk': pk})