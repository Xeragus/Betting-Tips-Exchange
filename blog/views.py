from django.shortcuts import render
from . models import BettingTip
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
)

# Create your views here.
def home(request):
    context = {
        'tips': BettingTip.objects.all()
    }
    return render(request, 'blog/home.html', context)

class HomeListView(ListView):
    model = BettingTip
    template_name = 'blog/home.html'
    context_object_name = 'tips'
    ordering = ['date_posted']

class BettingTipDetailView(DetailView):
    model = BettingTip

class BettingTipCreateView(LoginRequiredMixin, CreateView):
    model = BettingTip
    fields = ['home_team', 'away_team', 'prediction', 'odds', 'analysis']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BettingTipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BettingTip
    fields = ['home_team', 'away_team', 'prediction', 'odds', 'analysis']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BettingTipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BettingTip
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
