from django.urls import path
from . import views
from django.conf.urls import url


'''
url(r'^$', views.index, name='index'):
    r'^$' – регулярное выражение = любая пустая строка. Смотрим на пустую строку, так как это второе url-преобразование
    первое уже отработало и обработало предыдущую часть url, так что сюда может быть доставлен пусто путь
    views.index – какое отображение звать по этому url
    name='index' – имя для этого преобразования, чтобы его (преобразование) можно было использовать позднее

url(r'^books/$', views.BookListView.as_view(), name='books'):
    r'^books/$' – обрабатывает все, где есть кусок "books/"
    views.BookListView.as_view() – также идет во views, так ищет BookListView, но это не функция, а класс. Чтобы
    обработать класс аналогично функции, надо вызвать на него .as_view()

url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'):
    r'^books/(?P<pk>\d+)$' – это регулярное выражение не просто просматривает url, но и захватывает его часть, а затем
    передает ее в отображение (view). Захватывать надо так: "?P<как передавать>что хватать".
    Соответственно:
        хватаем "\d+" – любые йифры в любом количестве
        передаем как pk – отображение ждет именно pk в данном случае, но можно передавать в другие места другие
        переменные или безымянные объекты.
'''


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]
