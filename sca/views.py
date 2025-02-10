from django.shortcuts import render
from django.utils import timezone
from .models import Usuario

# Create your views here.

def sca_list(request):
    usuarios = Usuario.objects.filter(data_alteracao__lte=timezone.now()).order_by('data_alteracao')
    return render(request, 'sca/sca_list.html', {'users':usuarios})
