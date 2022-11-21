#Name: Kerry Flowers
#Program Purpose: This program finds the cost of pizza
#   Sales tax rate: 5.5%

import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
S_SMALL = 9.99
M_MEDIUM = 12.99
L_LARGE = 14.99
X_EXTRA_LARGE = 17.99

# define global variables
pizza_size = "L"
num_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ################
def main() :
    order_again = True
    while order_again:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Would you like to order again? ")
        if yesno == "N" or yesno == "n":
            print("Thank you for ordering from Palermo Pizza")
            order_again = False
            return()

def get_user_data():
    global num_pizza, pizza_size
    pizza_size = input("Palermo Pizza Sizes:\n\tS for Small \n\tM for Medium \n\tL for Large \n\tX for Extra Large: \nWhat size pizza? ")    
    num_pizza = int(input("How many pizzas? "))

def perform_calculations():
    global subtotal, sales_tax, total,num_pizza, pizza_size
    if pizza_size == "S" or pizza_size == "s":
        subtotal = num_pizza * S_SMALL
    if pizza_size == "M" or pizza_size == "m":
        subtotal = num_pizza * M_MEDIUM
    if pizza_size == "L" or pizza_size == "l":
        subtotal = num_pizza * S_SMALL
    if pizza_size == "X" or pizza_size == "x":
        subtotal = num_pizza * S_SMALL

        
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('**** Palermo Pizza ****')
    print('Your neighborhood pizza house')
    print('-------------------------------')
    print('Pizza      $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax  $ ' + format(sales_tax,'8,.2f'))
    print('Total      $ ' + format(total,'8,.2f'))
    print('--------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()

