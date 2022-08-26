from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books
from django.urls import reverse
from django.http import HttpResponseRedirect

#loads the index page
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

#takes the user to the results page
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

#takes the user to the add page
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

#used to add a book, x is the book name, y is the book author
def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    book = Books(book_name = x, book_authorName=y)
    book.save()
    return HttpResponseRedirect(reverse('index'))

#used to delete a book, takes the id as an argument and deletes it
def deleterecord(request, id):
    books = Books.objects.get(book_id=id)
    books.delete()
    return HttpResponseRedirect(reverse('index'))
