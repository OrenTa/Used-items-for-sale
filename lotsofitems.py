from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Item, Base, Category, User

engine = create_engine('sqlite:///cataloglisting.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create six categories
clothes = Category(name="Clothes")
furniture = Category(name="Furniture")
pets = Category(name="Pets")
vehicles=Category(name="vehicles")
powertools=Category(name="power tools")
books=Category(name="books")

session.add(clothes)
session.commit()
session.add(furniture)
session.commit()
session.add(pets)
session.commit()
session.add(vehicles)
session.commit()
session.add(powertools)
session.commit()
session.add(books)
session.commit()

 
print "added menu items!"
