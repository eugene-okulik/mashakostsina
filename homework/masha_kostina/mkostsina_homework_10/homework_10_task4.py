
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()
goods = new_list[::2]
price = [int(price[:-1]) for price in new_list[1::2]]
new_dict = dict(zip(goods, price))

print(new_dict)
