from django.urls import path
from . import views
from .views import (
            HomeListView,
            BettingTipDetailView,
            BettingTipCreateView,
            BettingTipUpdateView,
            BettingTipDeleteView,
            ProfileBettingTipListView,
)

urlpatterns = [
    path('', HomeListView.as_view(), name='dashboard'),
    path('betting-tip/<int:pk>/', BettingTipDetailView.as_view(), name='tip-detail'),
    path('betting-tip/new', BettingTipCreateView.as_view(), name='tip-create'),
    path('betting-tip/<int:pk>/update', BettingTipUpdateView.as_view(), name="tip-update"),
    path('betting-tip/<int:pk>/delete', BettingTipDeleteView.as_view(), name="tip-delete"),
    path('profile/<str:username>', ProfileBettingTipListView.as_view(), name="profile-detail"),
]
