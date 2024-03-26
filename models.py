import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=50), unique = True)

    def __str__(self):
        return f'{self.id}| {self.name}'


class Book(Base):
    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'{self.id}| {self.title}| {self.id_publisher}'


class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), nullable=False)

    def __str__(self):
        return f'{self.id}| {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('Book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('Shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    books1 = relationship(Book, backref='stocks1')
    shopes1 = relationship(Shop, backref='stocks2')

    def __str__(self):
        return f'Stock {self.id}|, {self.id_book}|, {Shop.name}|, {self.count}'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    data_sale = sq.Column(sq.Text)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)

    stocks3 = relationship(Stock, backref='sales1')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)







