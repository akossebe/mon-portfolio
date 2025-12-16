from django.shortcuts import render

def index(request):
    context = {
        "nom": "Mouktar",
        "universite": "Université de Yaoundé I",
        "filiere": "Technologie de l’Information et de la Communication (ICT)",
        "message": "Bienvenue sur mon premier portfolio Django"
    }
    return render(request, 'portfolio/index.html', context)

from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
