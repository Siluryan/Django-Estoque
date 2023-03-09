from django.shortcuts import render
from registro.models import Nota

def index(request):
    """View function for home page of site."""

    num_notas = Nota.objects.all().count()    

    context = {
        'num_notas': num_notas, 
    }

    return render(request, 'index.html', context=context)

