from django.shortcuts import render
#from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage.html')

def author(request):
    return render(request, 'author.html')
    #return HttpResponse ('<h1>The author is Cesar</h1>')