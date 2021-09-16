from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


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

    # 2 строчки ниже нужны, чтобы показывать, сколько раз пользователь посетил эту страницу
    # получаем значение сессии в num_visits. Если там пусто, то вернется 0 (указан вторым аргументом)
    # num_visits мы передадим к шаблон (render, ниже), вставив ее в контекст
    num_visits = request.session.get('num_visits', 0)
    # затем мы переписываем это значение, добавляя к нему 1
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request,
                  'index.html',
                  context={'num_books':num_books,
                           'num_instances':num_instances,
                           'num_instances_available':num_instances_available,
                           'num_authors':num_authors,
                           'num_genres':num_genres,
                           'num_visits': num_visits
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


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')