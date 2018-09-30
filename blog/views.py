from django.shortcuts import render, get_object_or_404
from . models import BettingTip
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
)

# Create your views here.

class HomeListView(ListView):
    model = BettingTip
    template_name = 'blog/home.html'
    context_object_name = 'tips'
    ordering = ['date_posted']
    paginate_by = 3

class BettingTipDetailView(DetailView):
    model = BettingTip

class ProfileBettingTipListView(ListView):
    model = BettingTip
    template_name = 'users/profile_detail.html'
    context_object_name = 'tips'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BettingTip.objects.filter(author=user).order_by('-date_posted')

class BettingTipCreateView(LoginRequiredMixin, CreateView):
    model = BettingTip
    fields = ['home_team', 'away_team', 'prediction', 'odds', 'analysis']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BettingTipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BettingTip
    fields = ['home_team', 'away_team', 'prediction', 'odds', 'analysis']
    template_name = 'blog/bettingtip_update.html'

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
