#This code is heavily inspired from sir Rohan's code when we were learning during lab class but hopefully my comments will show that I do understand on how these code work.
from Menu import menu
def make_list():
    shopping_list=[] #a list that will contain everything from the user input below
    

    while True:
        number_amount=eval(input("Amount of items to be bought: ")) 
        if number_amount<1: #in order to make sure that the customer using the system will buy more than one and eliminate the chance of an error from the system
            print("One item must be bought at the least.")
        else:
            break #in order for the code to not repeat the while loop we have the break command

    for i in range (number_amount): #This will repeat the code below as much as the user specied in item that is going to be bought
        while True: #using a loop so that if in any case the user entered a number that does not meet the spec, it would rerun the code until the user enter a valid number
            item_name=input("Name of Item: ")
            mass= eval(input("Enter number of pounds: "))
            item=menu(item_name,mass) #in order import the dictionary that is stored in a different file
            if item_name=="" or item.get_price()==0: #in order for the computer to not accept empty strings or empty integers
                    print("You need to enter a valid name.")
            elif mass<0:
                    print("amount has to be more than 0")
            else:
                break #in order for the code to not repeat the while loop we have the break command
        shopping_list.append(item) #to add the above value from the user input into the list

    return shopping_list #in order to allow the shopping_list.append to be returned into the global code instead of just residing inside the loop

def display(item_list): #Creating a final reciept for the user
    print("---------------------------------") #to create a line in which we can seperate the user input and the final data sheet for the sake of the user.
    print("These are the items that you have purchased:")
    for i in range(len(item_list)): #above the user has the option of how many item does the user want to buy this code will repeat the code below until the number of item have been reach
        print(f"Item {i+1}") #To print how many item the user has bought, learnt that you can actually do this from the prograte JS course
        print(item_list[i].total_price()) #Single price of each item bought
    

def cost_total(item_list):
    total=0 #for now we give it a zero because later on we can replace the zero with our variable
    for i in range(len(item_list)): #will run this code as much as the amount of item the user have bought
        total += item_list[i].total_price() #this variable will allow the code to input the total price 
        return total #in order to return this variable from inside the function to outside of it.

shopping_list=make_list() #this will tell the computer to make a list as defined from above
display(shopping_list) #will make the reciept with the content being from the shopping_list variable
print(f"Total amount: ${cost_total(shopping_list)}") #will print the the total amount of money required to purchase the items


