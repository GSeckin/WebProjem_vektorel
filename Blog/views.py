from django.shortcuts import render,get_object_or_404
from .models import Gonderi
from .forms import GonderiForm

def gonderi_liste(request):
    Gonderiler = Gonderi.objects.all()
    return render(request, 'GorkemBlog/gonderi_liste.html', {'Gonderis':Gonderiler})

def gonderi_detay(request,pk):
    yazi = get_object_or_404(Gonderi,pk=pk)
    return render(request, 'GorkemBlog/gonderi_detay.html', {'gonderi':yazi})
    
def yeni_gonderi(request):
    Form = GonderiForm()
    return render(request, 'GorkemBlog/gonderi_duzenle.html', {'form': Form})