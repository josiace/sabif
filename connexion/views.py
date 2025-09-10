from django.shortcuts import render


# Create your views here.
def creer(request):
      
    return render(request, 'creat_compt.html',)


def connecter(request):
    return render(request, 'compt.html',)

def mon(request):
    
    return render(request, 'mon.html')