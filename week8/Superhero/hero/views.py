from django.views.generic import ListView, TemplateView
from .models import Hero
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(TemplateView):
    model = Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}


class IndexView(TemplateView):
    template_name = 'index.html'

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero_add.html'
    fields = ['name', 'identity', 'image', 'description']

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = ['name', 'identity', 'image', 'description']

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')