from django.shortcuts import render
from django.http import HttpResponse, Http404

# books = [
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Liff' 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladie\'s Detective Agency' 'author': 'Alexander McCall Smith'}
# ]

from .models import Book

def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, 'books/404.html', data)

# Create your views here.
def home(request):
    data = { 'books' : Book.objects.all() }
    # return HttpResponse(f'test')
    print(data)
    return render(request, 'books/home.html', data)


# @login_required
# def create(request, book_id):
#         book = get_object_or_404(Book, pk=book_id)
#         if request.method == 'POST':
            
        


# def show(request, id):
#     # book = get_object_or_404(Book, pk=id)
#     return HttpResponse('this path works')
    
   

