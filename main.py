
class Customer:
    def __init__(self, name, surname, email, birthday):
        self.name = name
        self.surname = surname
        self.email = email
        self.birthday = birthday
    def __str__(self):
        return "Name: %s, Surname: %s, Email: %s, Birthday: %s" % (self.name, self.surname, self.email, self.birthday)

customerDataBase = {} 

# Initial random customers to have in Data Base.
customerDataBase[1] = Customer("Robert", "Alain", "ralain@gmail.com", "21/10/1995")
customerDataBase[2] = Customer("Ruben", "Zafra", "rzafra@gmail.com", "25/05/1994")
customerDataBase[3] = Customer("Claudia", "Ramon", "cramon@gmail.com", "13/12/1995")

def whatToDo():
    print("\nCreate a new customer. A customer must have the following attributes: name, surname, email and birthdate.-> create\n"
          "Get a single customer with all the attributes mentioned above -> get\n"
          "Get all customers. For each customer, the same information must be obtained as in the previous point -> getAll\n"
          "Update all the attributes (at once) of an existing customer mentioned above -> update\n"
          "Delete an existing customer -> delete\n\n")
    x = input("What do you want to do: ")
    match x:
        case "create": 
            createCustomer()
        case "get":
            getCustomer()
        case "getAll":
            getAllCustomers()
        case "update":
            updateCustomer()
        case "delete":
            deleteCustomer()
        case "exit":
            stopcrm()
        case _:
            print("Please put a valid command")

def stopcrm():
    raise Exception("Logged out")

def createCustomer():
    name = input("Type customer name: ")
    surname = input("Type customer surname: ")
    email = input("Type customer email: ")
    birthday = input("Type customer birthday(dd/mm/yyyy): ")
    customerDataBase[len(customerDataBase) + 1] = Customer(name, surname, email, birthday)

# I went with email because I thought it was the unique feature of every customer (I could do one function for each attribute, getCustomerFromID, getCustomerFromName,etc)
def getCustomer():
    searchEmail = input("Insert customer email: ")
    c = None
    for id, customer in customerDataBase.items():
        if searchEmail == customer.email:
            c = customer            
    if c != None:
        print(c)
    else: 
        print("Not a valid email.")

def getAllCustomers():
    for id, customer in customerDataBase.items():
        print(customer)

# As it is an API I thought it would be more useful to do it with ID, but you can do it like above by any attribute
def updateCustomer():
    customerID = int(input("Insert customer ID: "))
    for id, customer in customerDataBase.items():
        if customerID == id:
            customer.name = input("Insert new name: ")
            customer.surname = input("Insert new surname: ")
            customer.email = input("Insert new email: ")
            customer.birthday = input("Insert new birthday: ")

def deleteCustomer():
    customerID = int(input("Insert customer ID: "))
    customerToDelete = None
    for id, customer in customerDataBase.items():
        if customerID == id:
            customerToDelete = id
    del customerDataBase[customerToDelete] 

                
while True:
    whatToDo()