import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = 'postgresql://postgres:4815162342@localhost:5432/postgres'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
#
# publisher1 = Publisher(name='Пушкин А.С.')
# publisher2 = Publisher(name='Толстой Л.Н.')
# book1 = Book(title='Капитанская дочка', publisher=publisher1)
# book2 = Book(title='Руслан и Людмила', publisher=publisher1)
# book3 = Book(title='Евгений Онегин', publisher=publisher1)
# book4 = Book(title='Война и мир', publisher=publisher2)
# book5 = Book(title='Анна Каренина', publisher=publisher2)
# book6 = Book(title='Детство', publisher=publisher2)
# shop1 = Shop(name='Буквоед')
# shop2 = Shop(name='Лабиринт')
# shop3 = Shop(name='Книжный дом')
# stock1 = Stock(books1=book1, shopes1=shop1, count=5)
# stock2 = Stock(books1=book2, shopes1=shop1, count=4)
# stock3 = Stock(books1=book3, shopes1=shop2, count=6)
# stock4 = Stock(books1=book4, shopes1=shop3, count=5)
# stock5 = Stock(books1=book5, shopes1=shop1, count=5)
# stock6 = Stock(books1=book6, shopes1=shop2, count=8)
# stock7 = Stock(books1=book6, shopes1=shop3, count=4)
# stock8 = Stock(books1=book1, shopes1=shop2, count=5)
# stock9 = Stock(books1=book1, shopes1=shop3, count=9)
# stock10 = Stock(books1=book2, shopes1=shop3, count=2)
# stock11 = Stock(books1=book2, shopes1=shop2, count=2)
# stock12 = Stock(books1=book3, shopes1=shop1, count=1)
# stock13 = Stock(books1=book3, shopes1=shop3, count=4)
# sale1 = Sale(price=500.50, data_sale='29.02.2020', stocks3=stock1, count=10)
# sale2 = Sale(price=504.50, data_sale='30.03.2020', stocks3=stock2, count=10)
# sale3 = Sale(price=600.50, data_sale='31.01.2020', stocks3=stock3, count=20)
# sale4 = Sale(price=610.50, data_sale='31.01.2020', stocks3=stock4, count=20)
# sale5 = Sale(price=410.70, data_sale='31.05.2020', stocks3=stock5, count=20)
# sale6 = Sale(price=450.70, data_sale='31.07.2020', stocks3=stock6, count=30)
# sale7 = Sale(price=480.90, data_sale='31.08.2020', stocks3=stock7, count=30)
# sale8 = Sale(price=680.20, data_sale='30.09.2020', stocks3=stock8, count=30)
# sale9 = Sale(price=630.20, data_sale='30.10.2020', stocks3=stock9, count=30)
# sale10 = Sale(price=615.20, data_sale='30.11.2020', stocks3=stock10, count=40)
# sale11 = Sale(price=635.20, data_sale='30.12.2020', stocks3=stock11, count=40)
# sale12 = Sale(price=545.10, data_sale='30.01.2021', stocks3=stock12, count=40)
# sale13 = Sale(price=565.10, data_sale='28.02.2021', stocks3=stock13, count=40)
#
# session.add_all([publisher1, publisher2,
#     book1, book2, book3, book4, book5, book6,
#     shop1, shop2, shop3,
#     stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13,
#     sale10, sale13, sale12, sale11, sale7, sale5, sale9, sale8, sale6, sale3, sale4, sale2, sale1])
# session.commit()

# publisher_name = input('Введите ФИО писателя: ')
#
# sales = (
#             session
#             .query(Sale.stocks3)
#             .join(Stock.books1)
#             .join(Stock.shopes1)
#             .join(Book.publisher)
#             .join(Publisher)
#             .filter(Publisher.name == publisher_name)
#             .all()
#         )
#
# for sale in sales:
#     print(f"{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {sale.data_sale}")

def get_sales(aauthor):
    poisk = session.query(Book.title, Shop.name, Sale.price, Sale.data_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    if aauthor.isdigit():
        zept = poisk.filter(Publisher.id == aauthor).all()
    else:
        zept = poisk.filter(Publisher.name == aauthor).all()
    for a,b,c,d in zept:
        # print(f'{a:<40} | {b:<10} | {c:<8} | {d.strftime("%d-%m-%Y")}')
        print(f'{a:<40} | {b:<10} | {c:<8}')
if __name__ == '__main__':
    pub = input("Введите ФИО писателя или его ID: ")
    get_sales(pub)

