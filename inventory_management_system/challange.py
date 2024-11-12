
                           ############ #Q1 adding numbers ##############

# def adding_number():
#     num1:str=input("Enter the number1 :")
#     num1:int=int(num1)

#     num2:str=input("Enter the number2 :")
#     num2:int=int(num2)

#     result:int = num1+num2

#     print("result :",result)
    
# adding_number()

#                           ############# #Q2  ##############

# def questing():
#     favourite:str=input("What is your animal? ")
#     print(f"My favourite animal is also {favourite}")
# questing()
#                     

                               ############# #Q3  ##############

# tem_fahrenheit :float=float(input("Enter the temperatire in fehrenheit :"))
# degree_celsius:float=(tem_fahrenheit-32)*(5.0/9.0)

# print(f"tempearute :{degree_celsius}C")


                               ############# #Q4  ##############

# Aunton :int=21
# Beth :int=6+Aunton
# Chen :int=20+Beth
# Drew :int=Chen+Aunton
# Ethan :int=Chen

# print(f"Auton is :{Aunton}\nBeth is {Beth}\nChen is {Chen}\nDrew is {Drew}\nEthan is {Ethan}")


                               ############# #Q5  ##############

# BOLD = "\033[1m"
# ITALIC = "\033[3m"
# length1 :float=float(input(f"{ITALIC}Enter the length1 of triangle : "))
# length2 :float=float(input(f"{ITALIC}Enter the length2 of triangle : "))
# length3 :float=float(input(f"{BOLD}Enter the length3 of triangle : "))
# perimeter:float=length1+length2+length3
# print(f"perimeter :{perimeter}")


                               ############# #Q6  ##############

# ITALIC = "\033[3m"
# length1 :int=int(input(f"{ITALIC}Enter the number :"))
# print(f"square :{length1**2}")


                            ###########################  Expressions ##########################

                               ############# #Q1  ##############
# import  random

# def roll_dice():
#     dice1 :int=random.randint(1,6)
#     dice2 :int =random.randint(1,6)
#     return dice1,dice2

# def main():
#  for roll in range(3):
#     dice1,dice2=roll_dice()
#     print(f"roll{roll+1}:\n{dice1}\n{dice2}")

# main()


                               ############# #Q2  ##############

# BOLD = "\033[1m"
# ITALIC = "\033[3m"
# mass :float=float(input(f"{BOLD}{ITALIC}Enter the mass in KG :"))
# c=299792458

# e=mass*c**2

# print(f"mass : {mass}\nspeed : {c}m/s\nenrgy : {e}J")



                               ############ #Q3  ##############


# inches_in_foot: int = 12  # Conversion factor. There are 12 inches for 1 foot.

# def main():
#     feet: float = float(input("Enter number of feet: "))  
#     inches: float = feet * inches_in_foot 
#     print(f"{inches}inches!")
    
# main()


#                                ############ #Q4  ##############
# import math

# BOLD = "\033[1m"
# ITALIC = "\033[3m"

# side1:float=float(input(f"{BOLD}{ITALIC}Enter the side1 length :"))
# side2:float=float(input(f"{BOLD}{ITALIC}Enter the side2 length :"))

# side3=math.sqrt((side1**2 + side2**2))

# print(f"hypotenuse :{side3}")


#                                ############ #Q5  ##############


# BOLD = "\033[1m"
# ITALIC = "\033[3m"

# num1:int=int(input(f"{BOLD}{ITALIC}Enter the integer1 :"))
# num2:int=int(input(f"{BOLD}{ITALIC}Enter the integer2 :"))

# result=num1//num2
# reminder=num1%num2

# print(f"result:{result},reminder:{reminder}")



#                                ############ #Q6  ##############

# import random
# def roll_dice():
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)

#     total=dice1+dice2

#     print(f"dice1 :{dice1}\ndice2 :{dice2}\ntotal :{total}")
# roll_dice()


                               ############ #Q6  ##############

# days=365
# hours=24
# minutes=60
# seconds=60

# seconds_in_years=days*hours*minutes*seconds

# print(f"total seconds :{seconds_in_years}")

                               ############ #Q7  ##############


# sentence:str="Panaversity is fun. I learned to program and used Python to make my"


# BOLD = "\033[1m"
# ITALIC = "\033[3m"

# adjective:str=(input(f"{BOLD}{ITALIC}Enter the adjective :"))
# noun:str=(input(f"{BOLD}{ITALIC}Enter the noun :"))
# verb:str=(input(f"{BOLD}{ITALIC}Enter the verb :"))

# print(f"{sentence} {adjective} {noun} {verb}")



                            ###########################  list ##########################

                               ############ #Q1  ##############


# def addition(lis) ->int:
#     total:int=0
#     for i in lis:
#         total+=i
#     return total

# lis:list=[1,2,3,4,5,6]

# result:int=addition(lis)

# print(result)


                               ########### #Q2  ##############


# def addition(lis) ->int:
#     n:int=len(lis)
#     for i in range(n):
#         index=lis[i]
#         lis[i]=index*2
#     print(lis)
    

    


    
# lis:list=[1,2,3,4,5,6]
# result:int=addition(lis)


                               ########### #Q5  ##############

# def get_first(lis):
#     print(lis[0])


# def get_lis():

#     lis=[]

#     # element:str=input("Enter the element or press enter to stop :")

#     element:str=input("Enter the element or press enter to stop :")

#     while element!="":
#      lis.append(element)
#      element:str=input("Enter the element or press enter to stop :")
#     return lis


# def main():
#     lst = get_lis()
#     get_first(lst)
#     print(lst)
# main()



                               ########## #Q6  ##############

# def get_last(lis):
#     print(lis[-1])


# def get_lis():

#     lis=[]

#     # element:str=input("Enter the element or press enter to stop :")

    

#     while True:
#      element:str=input("Enter the element or press enter to stop :")
#      if element=="":
#         break
#      lis.append(element)
#     return lis


# def main():
#     lst = get_lis()
#     get_last(lst)
#     print(lst)
# main()


                               ######### #Q7  ##############


# def get_lis():

#     lis=[]

#     # element:str=input("Enter the element or press enter to stop :")

    

#     element:str=input("Enter the element or press enter to stop :")
#     while element!="":
#      lis.append(element)
#      element:str=input("Enter the element or press enter to stop :")
#     return lis


# def main():
#     lst = get_lis()
#     print(lst)
# main()
   

                    ################## dictinary ####################

# def func():
#     dic={}
#     lis=[1,1,3,3,5,3,3,8,8,9,10]
    
#     for i in lis:
#         if i not in dic:
#          num=lis.count(i)
#          dic[i]=num
#     print(dic)
# func()
    




                     ############## function ###############

#Q1

# def average(a:float,b:float):
    
#     sum=a+b
#     return sum/2

# def main():
    
#     avg=average(12,35)
#     print(avg)
# main()
    


#Q3

# def count(lst):
#     count=0
#     for i in range(len(lst)):
#      num=lst[i]
     

#      if int(num)%2==0:
#         count+=1
#     print(count)


# def get_lst():
#    lst=[]

#    user_input=input("Enter the integer or press enter to stop :")
#    while user_input!="":
#       lst.append(user_input)
#       user_input=input("Enter the integer or press enter to stop :")
#    return lst
      

# def main():
#    lst=get_lst()
#    count((lst))
# main()

#Q4

# def double(num:int):
#     return (num*2)

# def main():
#     num=int(input("Enter the number :"))
#     num_times=double(num)
#     print(num_times)
# main()


#Q5
# def get_nam():
#     name=input("Enter your name:")
#     return name

# def main():
#     name=get_nam()
#     print(f"hello {name}")
# main()


#Q6
            
# def is_odd(value: int):
    
#     remainder = value % 2 
#     return remainder==1


# def main():
#     for i in range(10):
#         if is_odd(i):
#             print(f"{i} odd")
#         else:
#             print(f"{i} even")
# main()


#Q7

# def print_divisor(num):
#     for i in range(num):
#         current_divisor=i+1
#         if num%current_divisor==0:
#             print(current_divisor)
   

# def main():
#     num=int(input("Enter the num to find divisor :"))
#     print_divisor(num)
# main()

# def print_multiple(message,repeats):
#     for i in range(repeats):
#         print(message)



# def main():
#     message=input("Enter the message :")
#     repeats=int(input("how many times to want to repeat :"))
#     print_multiple(message,repeats)

# main()

#Q9

# def make_sentence(word, part_of_speech):
#     if part_of_speech == 0:
        
#         print("I am excited to add this " + word + " to my vast collection of them!")
#     elif part_of_speech == 1:
        
#         print("It's so nice outside today it makes me want to " + word + "!")
#     elif part_of_speech == 2:
       
#         print("Looking out my window, the sky is big and " + word + "!")
#     else:
       
#         print("Part of speech must be 0, 1, or 2! Can't make a sentence.")


# def main():
#     word :  str = input("Please type a noun, verb, or adjective: ")
#     print("Is this a noun, verb, or adjective?")
#     part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
#     make_sentence(word, part_of_speech)
# main()

# #Q10
# def print_ones_digit(num): 
#    print("The ones digit is", num % 10)

# def main(): 
#    num = int(input("Enter a number: ")) 
#    print_ones_digit(num)
# main()



################## information flow ####################

#Q1
# adult_age=18
# def age_checking(age):
#     if age>=adult_age:
#         print("age entered is adult age")
#         return True
#     else:
#         print("age entered is not adult age")
#         return False
    
# def main():
#     age=int(input("Enter the age :"))
#     (age_checking(age))
# main()

#Q2

# There is no need to edit code beyond this point

# def greet(name):
#     return "Greetings " + name + "!"

# def main():
#     name : str = input("What's your name? ")
#     print(greet(name))


# main()

#Q3

# def in_range(n, low, high):
#  if n >= low and n <= high:
# 	     return True
#  else:
#     return False

    

#Q4




# def num_in_stock(fruit):
	
# 	if fruit == 'mango':
# 		return 2
# 	if fruit == 'grapes':
# 		return 4
# 	if fruit == 'pear':
# 		return 1000
# 	else:
		
# 		return 0

# def main():
# 	fruit : str = input("Enter a fruit: ")
# 	stock = num_in_stock(fruit)
# 	if stock == 0:
# 		print("This fruit is not in stock.")
# 	else:
# 		print("This fruit is in stock! Here is how many:")
# 		print(stock)
# main()



#Q5

# def subtract_seven(num):
# 	num = num - 7
# 	return num


# def main():
# 	num: int = 7
# 	num = subtract_seven(num)
# 	print("this should be zero: ", num)
# main()


################### loop control ####################

#Q1
# import random
# def main():
#     # Generate the secret number at random!
#     secret_number = random.randint(1, 99)
    
#     print("I am thinking of a number between 1 and 99...")
    
#     guess = int(input("Enter a guess: "))
   
#     while guess != secret_number:
#         if guess < secret_number:  # If-statement is True if guess is less than secret number
#             print("Your guess is too low")
#         else:
#             print("Your guess is too high")
            
#         print()
#         guess = int(input("Enter a new guess: ")) 
        
#     print(f"Congrats! The number was: {str(secret_number)}")


#Q2

# MAX_TERM_VALUE : int = 10000

# def main():
#     curr_term = 0  
#     next_term = 1  
#     while curr_term <= MAX_TERM_VALUE:
#         print(curr_term)
#         term_after_next = curr_term + next_term
#         curr_term = next_term
#         next_term = term_after_next

#Q3
# def main():
#     for i in range(20):
#         print(i * 2)  
# main()


#Q4

# AFFIRMATION : str = "I am capable of doing anything I put my mind to."

# def main():
#     print("Please type the following affirmation: " + AFFIRMATION)
#    #  user_feedback = input()  

#     while user_feedback != AFFIRMATION: 
#         print("That was not the affirmation.")

#         # Ask the user to type the affirmation again!
#         print("Please type the following affirmation: " + AFFIRMATION)
#         user_feedback = input()

#     print("That's right! :)")

# main()

































