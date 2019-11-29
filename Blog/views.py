from django.shortcuts import render,get_object_or_404
from .models import Gonderi

def gonderi_liste(request):
    Gonderiler = Gonderi.objects.all()
    return render(request, 'GorkemBlog/gonderi_liste.html', {'Gonderis':Gonderiler})

def gonderi_detay(request,pk):
    yazi = get_object_or_404(Gonderi,pk=pk)
    return render(request, 'GorkemBlog/gonderi_detay.html', {'gonderi':yazi})
    