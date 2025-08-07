
class Book:
    material_stranic = 'бумага'
    nalichie_texta = True

    def __init__(self, nazvanie, avtor, kol_stranic, isbn, reserv=False):
        self.nazvanie = nazvanie
        self.avtor = avtor
        self.kol_stranic = kol_stranic
        self.isbn = isbn
        self.reserv = reserv

    def info(self):
        if self.reserv:
            print(
                f'Название: {self.nazvanie}, Автор: {self.avtor}, страниц: {self.kol_stranic}, материал: {Book.material_stranic}, зарезервирована')
        else:
            print(
                f'Название: {self.nazvanie}, Автор: {self.avtor}, страниц: {self.kol_stranic}, материал: {Book.material_stranic}')


book1 = Book('Идиот', 'Достоевский', 500, '1_1')
book2 = Book('Преступление и Наказание', 'Достоевский', 499, '1_2')
book3 = Book('Война и мир', 'Тостой', 498, '2_1', True)
book4 = Book('Анна Каренина', 'Толстой', 497, '2_2')
book5 = Book('Чазения', 'Караткевич', 496, '3_1')

books = [book1, book2, book3, book4, book5]
for book in books:
    book.info()


class Uchebniki(Book):

    def __init__(self, nazvanie, avtor, kol_stranic, isbn, predmet, shk_class, zadanie, reserv=False):
        super().__init__(nazvanie, avtor, kol_stranic, isbn, reserv)

        self.predmet = predmet
        self.shk_class = shk_class
        self.zadanie = zadanie


    def info(self):
        if self.reserv:
            print(
                f'Название: {self.nazvanie}, Автор: {self.avtor}, страниц: {self.kol_stranic}, предмет: {self.predmet}, класс: {self.shk_class}, зарезервирована')
        else:
            print(
                f'Название: {self.nazvanie}, Автор: {self.avtor}, страниц: {self.kol_stranic}, предмет: {self.predmet}, класс: {self.shk_class}')


uchebnik1 = Uchebniki('Математика', 'Иванов', 500, '1_1_1', 'Математика', 5, False)
uchebnik2 = Uchebniki('История', 'Петров', 499, '2_1_1', 'История', 9, False)
uchebnik3 = Uchebniki('География', 'Сидоров', 498, '3_1_1', 'География', 7, True, True)
uchebnik4 = Uchebniki('Физика', 'Кузнецов', 497, '4_1_1', 'Физика', 8, True)
uchebnik5 = Uchebniki('Химия', 'Соловьевов', 496, '5_1_1', 'Химия', 10, False)

uchebniki = [uchebnik1, uchebnik2, uchebnik3, uchebnik4, uchebnik5]
for uchebnik in uchebniki:
    uchebnik.info()
