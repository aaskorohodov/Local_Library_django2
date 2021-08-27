from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    num_genres = Genre.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request,
                  'index.html',
                  context={'num_books':num_books,
                           'num_instances':num_instances,
                           'num_instances_available':num_instances_available,
                           'num_authors':num_authors,
                           'num_genres':num_genres
                           },
    )


class BookListView(generic.ListView):
    '''Это обобщенное отображение, оно сделает запрос к базе, получит все записи модели Book и отрисует шаблон.
    Обобщенное отображение по умолчанию ищет шаблон по имени /application_name/the_model_name_list.html
    То есть тут оно ожидает найти /locallibrary/catalog/templates/catalog/book_list.html что является ебаниной'''
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book