#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### It is a good time to get job of data analyst at wallmart. 
#Impress the recruiter through your programming skills by generating an interactive shopping bill for wallmart. 
#Feel free to use the concepts of lists, tuples, sets and dictionary to accomplish yourtask.

#SELF-CHECKOUT Wallmart 
#0. Loop -> Name(Customer db) + Membership code 
#1. Choose how to pay : Cash, Card, Others(Ask Clerk)
# function : lastly, pay bill in different way. 
# Cash -> Type Money, Show change,
# (Debit/ Credit)Card -> Before cheking out, insert cards, Installment(할부) 
#2. Choose bag size, and take it below the shelves. 
#3. Type product code refering below product table
# (Product code , qauntity) -> DICTIONARY 
# If done, press N(ext) in the product blank  
#4-1. Customer Check point : Number of products >> accept and move on to next step
# If need to be change, change... 
#4-2. Membership point + Coupon = total Amount
#5. >> Payment output(depends on method)
#6. Bill print(With Cafe Discount coupon)
import time, textwrap
from datetime import datetime

preferredWidth = 50
wrapper = textwrap.TextWrapper(width=preferredWidth , subsequent_indent=' '*3)

#membership id function
codeVerification_save = lambda x : int(x) if str(x).isnumeric() else 0  
bagprice_save = lambda x : int(x)*5 if str(x).isnumeric() else 0  

#Product data
products = [{"Lays(green)": 10} ,{"Lays(orange)": 10}, {"Timtam": 15}, {"Chocopie": 25} ,
             {"Napkin" : 30}, {"Bottle" : 20}, {"Cup" : 10}, {"Fork and spoon" : 15}, 
          {"Papaya" : 5}, {"Musk melon" :10}, {"Mango":7}, {"Blueberry" : 30}]

membership_code = (1309, 8857, 1218)
discount_code = [{1234 : 5}, {1000 : 10}, {3456 : 15}]

def inputCheck(choice, option) : 
    if choice not in range(1,option+1) : 
        print("WRONG CHARACTER. TRY AGAIN.")
        return -1

def printProducts() : 
    time.sleep(1)
    print("\n")
    print("============Shelves=============")
    cnt = 1 
    for product in products :
        for key, value in product.items() :
            pro_str = str(cnt) + ") " + str(key)
            print(pro_str.ljust(15), end ="")
            print(str(value).rjust(19))
            cnt += 1
    print("=================================")
    print("\n")


def printMyCart(name, cart) : 
    print("------------{} Cart-------------".format(name))
    for i in range(len(cart)) :
        for key, value in cart[i].items() :
            pro_str = "["+ str(i+1) + "] " + str(list(products[key-1].keys())[0])
            print( pro_str.ljust(17) , end =" ")
            print (str(value).rjust(17))
    print("----------------------------------")

def printTotalAmount(name, cart, discount, waytoPay) : 
    time.sleep(1)
    print("=============Sales================")
    print("  Product       Qty           Amt ")
    time.sleep(1)
    total_amount = 0
    total_piece = 0
    for i in range(len(cart)) :
        for key, value in cart[i].items() :
            
            product_str = "["+ str(i+1) + "] " + str(list(products[key-1].keys())[0])
            amount = value*int(list(products[key-1].values())[0])
            print( product_str.ljust(17), end =" ")
            print( str(value) , end =" ")
            total_amount += amount
            total_piece += value
            print (str(amount).rjust(14))
    print("----------------------------------")
    time.sleep(1)
    print("Total".ljust(12) , end ="")
    piece_str = str(total_piece) + " Pieces"
    print(piece_str.center(10), end ="") 
    print(str(total_amount).rjust(12)) 
    
    print("Payment".ljust(17), end = "")
    print(str(total_amount).rjust(17)) 
    print("Discount".ljust(17), end = "")
    print(str(discount).rjust(17)) 
    print("Bag".ljust(17), end = "")
    print(str(bagsize*5).rjust(17)) 
    total_amount -= discount
    total_amount += bagsize*5
    print("=================================")
    time.sleep(1)
    print("Total".ljust(17), end ="")
    print(str(total_amount).rjust(17)) 
    if waytoPay == 1: 
        waytoPayCash()
        print("Cash".ljust(17), end ="")
        print(str(total_amount).rjust(17)) 
        print("Change".ljust(17), end ="")
        print("0".rjust(17))
    elif waytoPay == 2: 
        print("Card".ljust(17), end ="")
        print(str(total_amount).rjust(17)) 
        print("Change".ljust(17), end ="")
        print("0".rjust(17))
    else: 
        print("Change".ljust(17), end ="")
        print(str(total_amount).rjust(17))
        print("Manager is coming...")
        print("XXX INCOMPLETE RECIEPT XXX".center(34))
 
    print("----------------------------------")
    time.sleep(1)
    print("-")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    print("Thank you for shopping with WallMart.")
    print("-")
    print("Customer complaints : \n010-4469-1800")
    print("WallMart Websites : \nwww.wallmart.com")

def waytoPayCash() : 
    print("Insert Cash.")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    
while True : 
    print("\n\n Hi! Welcome to WallMart! This is SELF-CHECKOUT Robot!")
    name = input("Type your name : ")
    #Save membership ID
    membership_input = input("[1] Enter your membership number. (If not, type No) : ")
    membership_id = codeVerification_save(membership_input)
    #Membership verification 
    if membership_id == 0 and membership_input != "No" : 
        print("WRONG MEMBERSHIP CODE. TRY AGAIN")
        continue
    if membership_id not in membership_code : 
        print("You are not member, Sign up later.")
        
    waytoPay = int(input("[2] Choose number how to pay (1) Cash (2) Card (3) Others(Call Person)"))
    
    if waytoPay == 2: 
        time.sleep(1)
        print("Before checking out, please insert card into the device.")
        time.sleep(1)
        print("...Checking...")
        time.sleep(1)
        
    if inputCheck(waytoPay,3) == -1 : 
        continue
        
    bagsize = int(input("[3] Select carry bag size. (1) S-5rp (2) M-10rp (3) L-15rp (4) No need "))
    if inputCheck(bagsize,4) == -1 : 
        continue
    if bagsize == 4 : 
        bagsize = 0 
    print("You can find carry bags under the shelves.")
    bagprice = bagprice_save(bagsize)
    
    printProducts()
    
    product_info = ""
    cart = []
    
    #Add to cart
    while True : 
        product_info = input("[4] Add to cart: enter index and quantity with SPACE BAR (If you move on to payment, enter 'X') :\n")
        
        # Move on to Payment 
        if product_info == "X" : 
            printMyCart(name, cart)
            checkid = input("Check your product list above. For payment press Y, for make change press N.")
            if checkid == "Y" : 
                time.sleep(1)
                print("Moving on to payment...")
                time.sleep(1)
                break
            elif checkid == "N" : 
                continue
            else : 
                print("ENTERED WRONG CHARACTER. TRY AGAIN.")
                continue
                
        # Add to cart 
        try : 
            prd_id, prd_qty = (product_info).split() #One value error 
        except ValueError : 
            print("ENTER INDEX AND QUANTITY. TRY AGAIN")
            continue
            
        if int(prd_id) in range(1, len(products)+1) and prd_qty.isnumeric() : # check if the product is in list              
            cart.append({int(prd_id):int(prd_qty)}) #Save product is selected
            printMyCart(name, cart)
        else : 
            print("ENTERED WRONG CHARACTER. TRY AGAIN.")
            continue
            
    # Discount step 
    discount_rp = 0 
    while True : 
        discount_input = input("\n[5] Enter discount code. If you don't have, press X.")
        if discount_input == "X" : 
            break 
        discount_id = codeVerification_save(discount_input)
        if discount_id == 0 : #If input is character not numeric 
            print("ENTERED WRONG CHARACTER. TRY AGAIN.") 
            continue
        for codeDic in discount_code : 
            for key, value in codeDic.items() : 
                if discount_id == key : 
                    print("Checked, "+ str(value)+ "rupees will be discounted. :)")
                    discount_rp = int(value)
        if discount_rp == 0 : 
            print("NOT MATCH DISCOUNT CODE..")
        if discount_rp > 0 : 
            break 
                    
    # Total Amount print 
    print("\n[6] Check your total amount.\n\n")
    time.sleep(1)
    printTotalAmount(name, cart, discount_rp, waytoPay)
    time.sleep(1)
            


# In[31]:


print("Juyoung".ljust(15), end ="")
print("1na".rjust(15))
print("2              na".rjust(25))


# In[25]:


products = [{"Lays(green)": 10} ,{"Lays(orange)": 10}, {"Timtam": 15}, {"Chocopie": 25} ,
             {"Napkin" : 30}, {"Bottle" : 20}, {"Cup" : 10}, {"Fork and spoon" : 15}, 
          {"Papaya" : 5}, {"Musk melon" :10}, {"Mango":7}, {"Blueberry" : 30}]

list(products[0].values())[0]


# In[40]:


tuple1 = (0,1,2)
tuple1.index(2)

