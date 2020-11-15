from django.shortcuts import render

# Create your views here.
def hello(request, number):
    context = {
        "number" : number
    }
    return render(request, 'home.html', context)

def index(request):
    return render(request, 'index.html')