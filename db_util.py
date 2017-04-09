from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Item, Base, Category, User

engine = create_engine('sqlite:///cataloglisting.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# options are:
# sc - show categories
# ac - add categories
# dc - delete categories
# si - show items (then it asks for which category)

print "\n-With this utility you can:\n-sc(show categories)\n-ac(add categories) \n-dc(delete category) \
        \n-si(show items)"

try:
    while True:
        s=raw_input("\n-What do you want to do?\n")
        if s=='sc':
            categories = session.query(Category).all()
            print "\n"
            print "the categories are: "
            for i in categories:
                print i.name
            print '\n'
        elif s=='ac':
            category_name=raw_input("\n-What is the name of the category?: ")
            new_cat=Category(name=category_name)
            session.add(new_cat)
            session.commit()
            print "\n- " + category_name + " added succesfuly!"
        elif s=='si':
            items=session.query(Item).all()
            s=1
            for i in items:
                print "(" + str(s)+")"
                print i.name
                print i.description
                print "price: " + str(i.price)
                print "by user: " + str(i.user_id)
                print "created on: " + str(i.created_date)
                print "category: " + str(i.category_id)
                print "\n"
                s=s+1
        else:
            print "-I'm not familiar with this command"
            print "\n-With this utility you can:\n-sc(show categories)\n-ac(add categories) \n-dc(delete category) \
                \n-si(show items)"
except:
    print "bye bye"
    
