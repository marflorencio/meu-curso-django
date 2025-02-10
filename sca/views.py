from django.shortcuts import render

# Create your views here.

def sca_list(request):
    return render(request, 'sca/sca_list.html', {})
