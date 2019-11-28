from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Name, Price, Picture_Link, Description):
    Product_object = Product(
        Name=Name,
        Price=Price,
        Picture_Link=Picture_Link,
        Description=Description)
    session.add(Product_object)
    session.commit()

def update_Price(name, Price):
   Product_object = session.query(
       Product).filter_by(
       Name=name).first()
   student_object.Price = Price
   session.commit()

def update_Price(name, Description):
   Product_object = session.query(
       Product).filter_by(
       Name=name).first()
   student_object.Description = Description
   session.commit()

def update_Picture_Link(name, Picture_Link):
   Product_object = session.query(
       Product).filter_by(
       Name=name).first()
   student_object.Picture_Link = Picture_Link
   session.commit()
 
def delete_product(name):
   session.query(Product).filter_by(
       Name=name).delete()
   session.commit()

def query_all():
   Products = session.query(
      Product).all()
   return Products

def query_by_name(name):
   product = session.query(
       Product).filter_by(
       Name=name).first()
   return product

def Add_To_Cart(ProductID):
    Cart_object = Cart(
        ProductID=ProductID)
    session.add(Cart_object)
    session.commit()

# add_product("best hoodie" , 45 , "best_hoodie.jpeg" , "this is one of the most comfortable hoodies, buy it now!")
