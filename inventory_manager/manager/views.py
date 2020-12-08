from django.shortcuts import render, get_object_or_404
from .models import Asset


def home(request):
    context = {
        'assets': Asset.objects.all()
    }
    return render(request, 'manager/list.html',
                  context)
