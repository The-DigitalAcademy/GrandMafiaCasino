from sqlalchemy import create_engine, MetaData, Table, Column,insert, Integer, VARCHAR, update, delete

  
engine = create_engine("postgresql://postgres:postgres@localhost:5430/address_book_db")

# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)
  
# create a table schema
# create a table schema
details = Table(
    'details',meta , 
    Column('id', Integer, primary_key=True),
    Column('names', VARCHAR),
    Column('email', VARCHAR),
    Column('address', VARCHAR),
    Column('contact', VARCHAR),
    extend_existing=True
)

def insert_new():

    new_name = input("Enter Your Name and Surname: ")
    new_email = input("Enter Your Email: ")
    new_add = input("Enter Address: ")
    phone = input("Enter Phone Number: ")

    inserting = details.insert().values(names=new_name,email=new_email,address=new_add,contact=phone)
    engine.execute(inserting)
    print("Record Added Successfully")

def modify():

    name = input("Enter Name and Surname for Record you want to Modify:")
    new_name = input("Enter Your New Name and Surname: ")
    new_email = input("Enter Your New Email: ")
    new_add = input("Enter Your New Address: ")
    phone = input("Enter Your New Phone Number: ")

    updated = update(details).where(details.c.names == name).values(names=new_name,email=new_email,address=new_add,contact=phone)
    engine.execute(updated)
    print("Record Updated Successfully")

def delete_detail():
    
    name = input("Enter Name and Surname for Record you want to Delete:")
    to_delete = delete(details).where(details.c.names == name)
    engine.execute(to_delete)
    print("Record Deleted Successfully")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("###############################################")
print("Welcome to The Grand Mafia Address Book Service")
print("###############################################")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("What would you like to do:")

options = input(
        "1. Add details\n"
        "2. Modify details\n"
        "3. Delete details\n"
        "4. Exit\n"
    )

while options is not False:
    
    if options == '1':
        insert_new()
        break
    elif options == '2':
        modify()
        break
    elif options == '3':
        delete_detail()
        break
    else:
        print("Invalid Option, Please try again!")
        break
