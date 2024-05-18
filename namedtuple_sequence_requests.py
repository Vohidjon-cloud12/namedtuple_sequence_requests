from collections import namedtuple
import psycopg2
import requests
import json

# # product nomli namedtuple yaratamiz:
# Product = namedtuple('Product', ['id', 'name', 'price'])
#
# product1 = Product(id=1, name='Laptop', price=1500.00)
# product2 = Product(id=2, name='Smartphone', price=800.00)
# product3 = Product(id=3, name='Tablet', price=300.00)
# # Obyektlarni chop etish
# print(product1)
# print(product2.name)
# print(product3._asdict())
#
#
# # Named tuple yaratish:
# Product = namedtuple('Product', ['id', 'name', 'price'])
#
# product1 = Product(id=1, name='Laptop', price=1500.00)
# product2 = Product(id=2, name='Smartphone', price=800.00)
# product3 = Product(id=3, name='Tablet', price=300.00)
#
# # Named tuple metodlari
#
# # 1. _make(): Iterable dan yangi named tuple yaratish
# product_data = [4, 'Smartwatch', 200.00]
# product4 = Product._make(product_data)
# print(f"_make() metodi orqali: {product4}")
#
# # 2. _asdict(): Named tuple ni lug'atga aylantirish
# product1_dict = product1._asdict()
# print(f"_asdict() metodi orqali: {product1_dict}")
#
# # 3. _replace(): Named tuple ni yangi qiymatlar bilan almashtirish
# product1_new = product1._replace(price=1400.00)
# print(f"_replace() metodi orqali: {product1_new}")
#
# # 4. _fields: Named tuple maydonlarini ko'rsatish
# print(f"_fields atributi orqali: {Product._fields}")
#
#
# # Person nomli namedtuple yaratamiz:
#
# Person = namedtuple('Person', ['fullname', 'age', 'email'])
# Sherali = Person('Sherali Aliyev', 18, 'sher@gmail.com')
# Hasan = Person('Hasan Husanov', 35, 'hasanboy@mail.ru')
# Xakimjon = Person('Xakimjon Nomozov', 23, 'xakimjon@gmail.com')
# print(Sherali)
# print(Sherali.fullname)
# print(Sherali, '\n', Hasan, '\n', Xakimjon)
# print(Person._fields)
#
# # namedtuple ga default qiymat berish:
# Person = namedtuple('Person', 'name age email', defaults=[18,'sher@gmail.com'])
# person1 = Person('Sherali')
# print(person1)
#
# # nametuple._make(data) = nametuple(*data) :
# data = ('Hasanboy', 24, 'hasanboy_terminator@yahoo.com')
# 1-case
# person2 = Person._make(data)
# print(person2)
# 2-case
# person2 = Person(*data)
# print(person2)
#
# # nametuple._replace () metodi bilan namedtuple malumotlarini o'zgartirishimiz mumkin:
# Person = namedtuple("Person", "name age height", defaults=[72, 1.75])
# person3 = Person("Rano")
# rano = person3._replace(age=27, name='Ranoxon')
# print(person3._field_defaults)
#
# # asdict() metodini qo'llab , key-value shaklda print qilamiz:
# print(rano._asdict())
#
# # Namedtuple elementlariga nomi bilan murojaat qilish:
# Rectangle = namedtuple('Rectangle', 'width height')
# r = Rectangle(10, 20)
# print(f"Rectangle width: {r.width}, height: {r.height}")  # Rectangle width: 10, height: 20
#
#
# # Sequences:Sequences - bu elementlar ketma-ketligi bo'lib, ular index orqali boshqariladi.
# # Python’da bir necha turdagi sequences mavjud: list, tuple, range, va string.

# # 1-list:
# fruits = ['apple', 'banana', 'cherry']
# print(fruits[1])  # 'banana'
#
# my_list = [5, 10, 15, 20, 25, 30]
# # my_list[start,stop,step]
# print(my_list[3:5])
# print(my_list[0:5:2])
# print(my_list[::-1])
#
# # 2-tuple:
# coordinates = (10, 20)
# print(coordinates[0])  # 10
#
# # 3-Range:
# numbers = range(1, 10, 2)
# for number in numbers:
#     print(number)  # 1 3 5 7 9
# # 4-string:
# message = 'Hello Guys'
# for char in message:
#     print(char, end='\n')



# requests moduli bilan ishlash::: << https://dummyjson.com/products/ >> url manziliga so'rov yuboramiz
# requests.get() bilan malumotlar web saytdan olinadi:
# url = 'https://dummyjson.com/products/'
# r = requests.get(url)
# for product in r.json()['products']:
    # print(product)
# productni input orqali tanlab chiqaramiz:
# _ID=int(input('Enter a product ID: '))
# url = f'https://dummyjson.com/products/{_ID}'
# r = requests.get(url)
# print(r.status_code,r.text)
# print(r.json())


# https://dummyjson.com/users/  saytdan userlarni bazaga add qilamiz:

# conn = psycopg2.connect(dbname='n47',
#                         user='postgres',
#                         password='123',
#                         host='localhost',
#                         port=5432)
#
# create_table_products_query = """create table products(
#         id serial primary key ,
#         title varchar(255) ,
#         description text ,
#         price int,
#         discountPercentage float,
#         rating float ,
#         stock int,
#         brand varchar(255),
#         category varchar(200),
#         thumbnail varchar(255)
#
# );"""
#
# cur = conn.cursor()
# cur.execute(create_table_products_query)
# conn.commit()

# insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail)
# values (%s,%s,%s,%s,%s,%s,%s,%s,%s);


# for product in r.json()['products']:
#     cur.execute(insert_into_query, (
#         product['title'], product['description'], product['price'], product['discountPercentage'], product['rating'],
#         product['stock'], product['brand'], product['category'], product['thumbnail']))
#     conn.commit()

# select_query="""SELECT * FROM products;"""
# cur.execute(select_query)
# products = cur.fetchall()
# for product in products:
#     print(product)

#'https://api.github.com' malumotlarini olamiz:
# response = requests.get('https://api.github.com')
# data = response.json()
# formatted_data = json.dumps(data, indent=4)
# print(formatted_data)
