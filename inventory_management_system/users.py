from file_handler import FileHandler
from inventory import Inventory
import re

class Person:
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
        self.file_handler = FileHandler()
    
    def create_account(self):
     """Creates a new account with a unique email and stores credentials as 'username,email,password'."""
     content = self.file_handler.read_lines("user.txt")
     self.username = input("Enter your username: ")
    
     while True:
        self.email = self.validate_input("Enter email eg-(example@gmail.com): ", r"^[a-zA-Z\d_]+@gmail\.com$")
        self.password = self.validate_input("Enter password min 8 characters alteast one capital and special character : ", r"^(?=.*[A-Z])(?=.*\d)(?=.*[_&@])[A-Za-z\d@_&]{8,}$")
        
        existing_email = False
        for line in content:
            parts = line.strip().split(',')
            if len(parts) == 3 and self.email == parts[1]:  #checking if username email password are present and also compare email whcih is on second place (parts[1])
                existing_email = True
                break
        
        if existing_email:
            print("Email already exists.Try Again")
        else:
            credentials = f"{self.username},{self.email},{self.password}"
            self.file_handler.write_line("user.txt", credentials)
            print("Account created successfully!")
            break

    def validate_input(self, prompt, pattern):
        """Validates user input according to the provided regular expression pattern."""
        while True:
            user_input = input(prompt)
            if re.match(pattern, user_input):
                return user_input
            else:
                print("Invalid input format.")

    def login(self):
        """Logs in the user by checking their email and password against stored records."""
        content = self.file_handler.read_lines("user.txt")
        while True:
         self.email = self.validate_input("Enter email eg-(example@gmail.com): ", r"^[a-zA-Z\d_]+@gmail\.com$")
         self.password = input("Enter password min 8 characters alteast one capital and special character :")
        
         for line in content:
            _, email, password = line.strip().split(',')
            if self.email == email and self.password == password:
                print("Login successful!")
                return True
         print("Invalid email or password.")
         continue
        
        
    

class Admin(Person):
    def __init__(self, username=None, email=None, password=None):
        super().__init__(username, email, password)
        self.inventory = Inventory()

    def admin_create_account(self):
        self.create_account()

    def admin_login(self):
      return self.login()

    def add_item(self):
        self.inventory.add_items()

    def modify_item(self):
        self.inventory.modify_items()

    def delete_item(self):
        self.inventory.delete_item()
        
    def view_inventory(self):
        self.inventory.show_details()

class User(Person):
    def __init__(self, username=None, email=None, password=None):
        super().__init__(username, email, password)
        self.inventory = Inventory()

    def user_create_account(self):
     self.create_account()

    def user_login_account(self):
       return self.login()
    def view_inventory(self):
        self.inventory.show_details()

    def buy_item(self):
        self.inventory.purchase_item()

    def user_search_product(self):
        self.inventory.search_product()
