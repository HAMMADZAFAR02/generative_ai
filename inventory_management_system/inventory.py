from file_handler import FileHandler
import re   #using reguar expressions for ids and credentilal valaidations 
import os



class Product:
    product_details = {
        101: {"name": "Laptop", "quantity": 20, "price": 800, "category": "Electronics"},
        102: {"name": "Smartphone", "quantity": 35, "price": 500, "category": "Electronics"},
        103: {"name": "Headphones", "quantity": 15, "price": 100, "category": "Electronics"},
        104: {"name": "T-Shirt", "quantity": 50, "price": 20, "category": "Clothing"},
        105: {"name": "Jeans", "quantity": 40, "price": 35, "category": "Clothing"},
        106: {"name": "Sneakers", "quantity": 30, "price": 55, "category": "Shoes"},
        107: {"name": "Book", "quantity": 100, "price": 15, "category": "Books"},
        108: {"name": "Pen", "quantity": 200, "price": 2, "category": "Stationery"},
        109: {"name": "Notebook", "quantity": 150, "price": 5, "category": "Stationery"},
        110: {"name": "Coffee Mug", "quantity": 80, "price": 10, "category": "Kitchenware"}
    }
    
    def __init__(self, product_id=None, name=None, quantity=None, price=None, category=None):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.file_handler = FileHandler()

    def checking(self):
        """Checks if inventory file exists; if not, initializes it with default product details."""
        if not os.path.exists("inventory.json") or os.stat("inventory.json").st_size == 0:
            self.file_handler.write_file("inventory.json", self.product_details)

    
    def show_details(self):
        content=self.file_handler.read_file("inventory.json")
        print(f"{'ID':<8}{'Name':<15}{'Category':<15}{'Price':<10}{'Quantity':<10}")
        for id,item in content.items():
          print(f"{id:<8}{item['name']:<15}{item['category']:<15}{item['price']:<10}{item['quantity']:<10}")



    @staticmethod
    def id_validation():
        """Validates product ID input as a three-digit number."""
        while True:
            id = input("Enter the three-digit product ID: ")
            if re.match(r"^\d{3}$", id):
                return (id)
            else:
                print("Invalid ID format. Please enter a three-digit number.")

    @staticmethod
    def id_generator(content):
        #generate next to last key
        existing_ids = [int(id) for id in content.keys()]
        return max(existing_ids) + 1 if existing_ids else 101


    def quantity_price_valid(self, prompt, pattern):
        """Validates price and quantity input according to specified pattern."""
        while True:
            user_input = input(prompt)
            if not re.match(pattern, user_input):
                print("Invalid format. Try again.")
                continue
            return int(user_input)


class Inventory(Product):
  def __init__(self, product_id=None, name=None, quantity=None, price=None, category=None):
        super().__init__(product_id, name, quantity, price, category)

   
  def add_items(self):
        """Adds a new item to the inventory."""
        self.checking()   #initializing file
        
        content = self.file_handler.read_file("inventory.json") or {}
        self.show_details()
        print("choose items from above inventory")
        while True:
          self.product_id = self.id_generator(content)
        
          self.name = input("Enter product name: ")
          self.category = input("Enter category: ")
          self.price = self.quantity_price_valid("Enter price: ", r"^[1-9][0-9]*$")
          self.quantity = self.quantity_price_valid("Enter quantity grater than zero: ", r"^[1-9][0-9]*$")
        
          content[self.product_id] = {"name": self.name, "category": self.category, "price": self.price, "quantity": self.quantity}
          self.file_handler.write_file("inventory.json", content)
          print("Item added successfully!")
          choice=input("Add more items Press Y and other key for Termination :").upper()
          if choice != 'Y':
            break

  def modify_items(self):
    """Modifies specified attributes of an item in the inventory."""
    self.show_details()
    print("choose items from above inventory")
    content = self.file_handler.read_file("inventory.json")
    if content:
    
       while True:
         item_id = self.id_validation()
         if item_id in content.keys():
            break  # Exit loop if a valid ID is found
         else:
            print("ID not found. Please try again.")
            continue
    
       while True:
        # Prompt for attributes to modify
        input_attributes = input("Enter the attributes you want to modify (e.g., name price quantity): ").strip().split()
        invalid_attributes = [attr for attr in input_attributes if attr not in content[item_id]]
        
        if invalid_attributes:
            print(f"Invalid attributes specified: {', '.join(invalid_attributes)}")
            continue
        
        # Modify specified attributes
        for attribute in input_attributes:
            if attribute in ["price", "quantity"]:
                new_value = self.quantity_price_valid(f"Enter new value for {attribute}: ", r"^[1-9][0-9]*$")
            else:
                new_value = input(f"Enter new value for {attribute}: ").strip()
            
            # Update the attribute with the new value
            content[item_id][attribute] = new_value
        
        # Save updates and confirm continuation
        self.file_handler.write_file("inventory.json", content)
        print("Item modified successfully!")
        
        choice = input("Modify more attributes for this item? Press Y to continue or other key to finish: ").upper()
        if choice != 'Y':
            break
    else:
        print("You cannot modify first you make file if not exist and initilize it")
 
  def delete_item(self):
        """Deletes an item from the inventory based on the item ID."""
        self.show_details()
   
        print("choose items from above inventory")
        content = self.file_handler.read_file("inventory.json")
        if content:
         while True:
          item_id = self.id_validation()
        
          if item_id in content:
            # Remove item from dictionary
            del content[item_id]
            # Save updated content back to file
            self.file_handler.write_file("inventory.json", content)
            print("Item deleted successfully!")
            choice = input("Deleting more items? Press Y to continue or other key to finish: ").upper()
            if choice != 'Y':
               break
          else:
           print("Item ID not found in the inventory.")
           continue
        else:
           print("you cannot delete items first you inilize and make file if not exist!")
            


    
  def purchase_item(self):
        """Handles purchase transactions and updates inventory quantity."""
        choice=""
        self.show_details()
        print("choose items from above inventory")
        content = self.file_handler.read_file("inventory.json")
        while True:
         self.id = self.id_validation()
         if self.id not in content:
             print("id not found. Try again")
             continue
         self.quantity = self.quantity_price_valid("Enter quantity: ", r"^[1-9][0-9]*$")

         if self.quantity > content[self.id]["quantity"]:
            print("Not enough quantity available.")
            continue
         else:
            content[self.id]["quantity"] -= self.quantity
            print(f"Remaining stock for {content[self.id]['name']}: {content[self.id]['quantity']}")
            self.file_handler.write_file("inventory.json", content)
            choice = input("Purchasing more items? Press Y to continue or other key to finish: ").upper()
            if choice != 'Y':
               break
            
  def search_product(self):
      content = self.file_handler.read_file("inventory.json")
      while True:
       if not content:
            print("No products in the inventory.")
            continue
       else:
                
        # Unified keyword search for name and category
        keyword = input("Enter product name or category to search: ").strip().lower()

        results = []
        for product_id, product in content.items():
            # Filter by keyword matching in either 'name' or 'category'
            if keyword and keyword not in product["name"].lower() and keyword not in product["category"].lower():
                continue
          
            results.append((product_id, product))
        print(results)

        if results:
            print(f"{'ID':<8}{'Name':<15}{'Category':<15}{'Price':<10}{'Quantity':<10}")
            for product_id, product in results:
                print(f"{product_id:<8}{product['name']:<15}{product['category']:<15}{product['price']:<10}{product['quantity']:<10}")
            choice = input("Purchasing more items? Press Y to continue or other key to finish: ").upper()
            if choice != 'Y':
               break
        else:
            print("No matching products found.")
