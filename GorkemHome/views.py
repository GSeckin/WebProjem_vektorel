from django.shortcuts import render


def ana_sayfa(request):
    return render(request, 'GorkemHome/index.html', {})
    