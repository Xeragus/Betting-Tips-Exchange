from django.shortcuts import render
from . models import BettingTip

# Create your views here.
def home(request):
    context = {
        'tips': BettingTip.objects.all()
    }
    return render(request, 'blog/home.html', context)
