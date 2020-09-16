from django.urls import path
from .import views

urlpatterns = [
path('', views.home, name='books-home'),
# path('books/new/', views.create, name)



# path('books/<int:id>/', views.show, name='book-show')
]