from django.shortcuts import render, get_object_or_404

# agregamos el modelo que definimos en models.py
#        (class Componente(models.Model):)
from .models import Componente
#Como views.py y models.py están en el mismo directorio, simplemente usamos . y el nombre del archivo (sin .py).


def part_detail(request, pk):
    compo = get_object_or_404(Componente, pk=pk)
    return render(request, 'controlStock/part_detail.html', {'compo': compo})

def part_list(request):

        componentes = Componente.objects.all()

        return render(request, 'controlStock/stock_list.html', {'componentes': componentes})# Create your views here.
