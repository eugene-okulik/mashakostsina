
class Flowers:
    def __init__(self, name, color, stem_length, price, avg_lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.avg_lifespan = avg_lifespan

    def __repr__(self):
        return f'{self.name} ({self.color}, {self.stem_length} см, {self.price} руб, {self.avg_lifespan} дней)'


class Greens(Flowers):
    def __init__(self, name, color, stem_length, price, avg_lifespan):
        super().__init__(name, color, stem_length, price, avg_lifespan)


class Wildflowers(Flowers):
    def __init__(self, name, color, stem_length, price, avg_lifespan):
        super().__init__(name, color, stem_length, price, avg_lifespan)


class Aster(Flowers):
    def __init__(self, name, color, stem_length, price, avg_lifespan):
        super().__init__(name, color, stem_length, price, avg_lifespan)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_price(self):
        return sum(flower.price for flower in self.flowers)

    def wilting_time(self):
        return sum(flower.avg_lifespan for flower in self.flowers) / len(self.flowers)

    def __repr__(self):
        flowers_info = "\n".join(f"  - {str(flower)}" for flower in self.flowers)
        return f"Букет состоит из:\n{flowers_info}"

    def sort_flowers_lifespan(self):
        self.flowers.sort(key=lambda flower: flower.avg_lifespan)

    def sort_by_color(self, reverse=False):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self, reverse=False):
        self.flowers.sort(key=lambda flower: flower.stem_length, reverse=reverse)

    def sort_by_price(self, reverse=False):
        self.flowers.sort(key=lambda flower: flower.price, reverse=reverse)

    def find_flower(self, value):
        return [flower for flower in self.flowers if flower.avg_lifespan == value]


bergrass = Greens('Берграсс', 'зеленый', 70, 3, 14)
cornflower = Wildflowers('Василек', 'синий', 60, 6, 7)
chrysanthemus = Aster('Хризантема', 'белый', 50, 5, 20)
eucalyptus = Greens('Эвкалипт', 'серо-зеленый', 60, 9, 28)
chamomile = Wildflowers('Ромашка', 'белый', 30, 3, 10)
dahlia = Aster('Георгина', 'желтый', 100, 8, 10)

bouquet = Bouquet([bergrass, cornflower, dahlia])

total_price = bouquet.get_price()
print(f'Стоимость букета: {total_price} руб.')

wilting_time = round(bouquet.wilting_time())
print(f'Время увядания: {wilting_time} дней')

bouquet.sort_flowers_lifespan()
print(bouquet)

bouquet.sort_by_color()
print(bouquet)

bouquet.sort_by_price()
print(bouquet)

bouquet.sort_by_stem_length()
print(bouquet)

find_flower = bouquet.find_flower(14)
print("Результат поиска:", ", ".join(str(flower) for flower in find_flower))
