from users import Admin,User



user_obj=User()
admin_obj=Admin()

i=True

while i!=False:
      choice=""
      print("Press 1 for Admin Signup :")
      print("Press 2 for Admin Login :")
      print("Press 3 for User Sign up :")
      print("Press 4 for User Login :")
      print("Press T for termination")
      choice=input("Enter your choice :").upper()
      if choice=='1':
         admin_obj.admin_create_account()
      elif choice=='2':
          if (admin_obj.admin_login()):
             print("successfully enering")
             while True:
              choice1=""
              print("press A for adding products")
              print("press R removing product")
              print("press U for updating product_attrinutes")
              print("press V for viewing inventory")
              print("press E for exit")
              choice1=input("Enter your choice :").upper()
            
              if choice1=="A":
               admin_obj.add_item()
              elif choice1=="R":
                admin_obj.delete_item()
              elif choice1=="U":
                admin_obj.modify_item()
              elif choice1=="V":
                admin_obj.view_inventory()
              elif choice1=="E":
               break
              else:
                print("invalid choice")
                continue
            
      elif choice=="3":
          user_obj.user_create_account()

      elif choice=="4":
         if user_obj.user_login_account():
    
            while True:
             print("Enter 1 for viewng invemtory")
             print("Enter 2 for buying a product")
             print("Enter 3 for searching a product")

             print("Enter E for exit")
             choice3=input("Enter your choice :").upper()
             if choice3=="1":
               user_obj.view_inventory()
             elif choice3=="2":
               user_obj.buy_item()
             elif choice3=='3':
                 user_obj.user_search_product()
             elif choice3=="E":
               break
             else:
               print("invalid choice")
               continue

      elif choice=="T":
         i=False
      
      else:
         print("invalid choice")



