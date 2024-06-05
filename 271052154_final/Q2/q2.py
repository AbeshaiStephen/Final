class Property:
    def __init__(self, propertyID, name, location, description, price_per_night, availability):
        self.propertyID = propertyID
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.availability = availability
        self.proplst=[]
        
    def __str__(self):
        return f"{self.propertyID}, {self.name}, {self.location}, {self.description}, {self.price_per_night}, {self.availability}, {self.booked}"



class User:
    def __init__(self, name, password):
        self.name = name
        self.password =  password
        self.is_logged_in = False
    def login(self):
        if self.is_logged_in == False:
            self.is_logged_in = True
        else:
            print("Already logged in")
    def logout(self):
        if self.is_logged_in == True:
            self.is_logged_in = False
        else:
            print("Already logged out")
    def __str__(self):
        return f"{self.name}, {self.password}, {self.is_logged_in}"
class Host(User):
    def __init__(self, name, password):
        super().__init__(name, password)
    def login(self):
        username=input("enter your user name")
        password=input("enter your password")
        if self.name == username and self.password ==  password:
            super().login()
            print(" Host logged in")
            print(self.is_logged_in)
            if self.is_logged_in == True:
                propID=input("Please enter property ID")
                nameprop=input("Enter property name")
                location=input("Enter property location")
                description=input("Enter property description")
                price_per_night=input("Enter price per night")
                availability=input("Enter availability")
                prop=Property(propID, nameprop, location, description, price_per_night, availability)
                prop.proplst.append(prop)
                print(prop.proplst)

    def logout(self):
        super().logout()
        print("Host logged out")
class Guest(User):
    def __init__(self, name, password):
        super().__init__(name, password)

    def login(self):
        username=input("enter your user name")
        password=input("enter your password")
        if self.name == username and self.password ==  password:
            super().login()
            print(" Guest logged in")
            print(self.is_logged_in)
            if self.is_logged_in==True:

                bookingID=input("enter booking id")
                property=input("enter property id")
                guest=input("enter guest name")
                check_in=input("enter check in date")
                check_out=input("enter check out date")
                booking_status=input("enter booking status")
                b=Booking(bookingID, property, guest, check_in, check_out, booking_status)
                b.book()
    def logout(self):
        super().logout()
        print("Guest logged out")


class Booking:
    booklst=[]
    def __init__(self, bookingIDuser, property, guest, check_in, check_out, booking_status):
        self.bookingIDuser = bookingIDuser
        self.property = property
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.booking_status = booking_status
    def __str__(self):
        return f"{self.bookingIDuser}, {self.property}, {self.guest}, {self.check_in}, {self.check_out}, {self.booking_status}"
    def book(self):
        self.booking_status = "Booked"
        Booking.booklst.append(self)
        print(booklst)

if __name__ == "__main__":
    while True:
        print("Welcome to the Property Management System")
        print("1. Login")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("1. Host")
            print("2. Guest")
            choice1 = int(input("Enter your choice: "))
            if choice1 == 1:
                print("1. Login")
                print("2. Exit")
                choice2 = int(input("Enter your choice: "))
                if choice2 == 1:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    host = Host(username, password)
                    host.login()
                    print(host.is_logged_in)
                elif choice2 == 2:
                    break
            elif choice1 == 2:
                print("1. Login")
                print("2. Exit")
                choice2 = int(input("Enter your choice: "))
                if choice2 == 1:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    guest = Guest(username, password)
                    guest.login()
                    print(guest.is_logged_in)
                elif choice2 == 2:
                    guest.logout()
        elif choice == 2:
            print("Thank you for using the Property Management System")
