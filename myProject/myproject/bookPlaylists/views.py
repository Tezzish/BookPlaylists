from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def results(request):
    if(request.method == 'GET'):
        bookresults = Books.objects.all().values()
        template = loader.get_template('results.html')
        context = {
            'bookresults': bookresults,
        }
        print("OH OUI")
        return HttpResponse(template.render(context, request))
    else:
        print("OH NON")

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    book = Books(book_name = x, book_authorName=y)
    book.save()
    return HttpResponseRedirect(reverse('index'))