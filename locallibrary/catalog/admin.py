from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
'''Это стандартная регистрация моделей в админке. При этом Джанго сам выведет всякие поля для заполнения.
Ниже показано, как выбрать, какие поля показывать и в каком виде.'''


class BookInline(admin.TabularInline):
    model = Book
    exclude = ('isbn',)
    extra = 0
    '''Описание ниже. Exclude убирает вывод какого-то атрибута.'''


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    '''Выбираем, какие поля отображать'''
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    '''Закомментированная строчка меняет отображение полей в админке. В примере выше будет 3 строчки, а последнея
    будет состоять сразу из двух полей.'''

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name')}),
        ('Рождение и смерть', {'fields': ('date_of_birth', 'date_of_death')})
    )
    '''А это делить экран на разделы. Первый раздел не имеет имени (None), в нем имя автора. Второй раздел про 
    даты рождения и смерти.'''

    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)
'''Это ассоциативная регистрация. Ниже есть аналог (регистрация декоратором).'''


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1
    '''Это создает то, что мы будем отображать ниже. Tabular это расположение горизонтально, еще есть StackedInline,
    Это вертикально или как-то так. extra это сколько пустых доп полей показывать, т.е. он выведет заполненные
    экземпляры класса, и предложит сразу там что-то еще создать. Если поставить 0, то будут только заполненные, \
    создавать будет нельзя. Но это еще не все, ниже показано, как это теперь поместить в Book'''


'''Декоратор делает тоже самое, что и admin.site.register(Author, AuthorAdmin) выше.
admin.site.register(Author, AuthorAdmin) это ассоциативная регистрация, которая показывает, 
на что ссылается класс админ-панели'''
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    '''Поместить очень просто, вот так (inlines)'''


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    '''Выбираем поля для фильтрации по ним. При этом сбоку (справа) создается sidebar, где можно натыкать фильтры.'''
    fieldsets = (
                 (None, {'fields': ('book', 'imprint', 'id')}),
                 ('Availability', {'fields': ('status', 'due_back')})
    )