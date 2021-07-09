
#----create the inputs----:
quartNum = int(input("Number of quarts-------- "))
oilFilter = str(input("Oil filter? (Y or N) ---- "))

#----define given constants----:
serviceFee = 10.00
salesTax = 0.06         # 6%
oilPerQuart = 6.95
filterPrice = 7.56
volumeDiscount = 0.10   # 10%
addLine = "-------" #separation line in receipt
epaNotice = "Notice: The EPA recommends that you dispose of used motor oil at a certified recycling center."

#----Calculations----:
oilPrice = quartNum * oilPerQuart


#----if statements----:
if (quartNum > 6): #-----check for volume discount
    discountAmount = volumeDiscount * oilPrice # what will print on "Discount" line
    subtotal = oilPrice - discountAmount #start running the subtotal here
else:
    subtotal = oilPrice

if (oilFilter == 'Y'): #------ check for oil filter addition
    subtotal = subtotal + filterPrice
    """ we only care if the answer is Y,
        otherwise we add nothing -- therefore,
        no else statement is needed"""

#----Final calculations----:
subtotal = subtotal + serviceFee # ---- what number will print on the "subtotal" line
taxAmount = salesTax * subtotal # ---- what number will print on the "Tax" line
total = subtotal + taxAmount  # ---- what number will print on the "total" line

# we convert these to strings so we can keep the '$' in front of the number no matter how big it is
oilPriceStr = "$" + str(round(oilPrice,2))
totalStr = "$" + str(round(total,2))

#----Printing & checking for discounts----:
print("\nYour bill from BisonLube\n") #----add newline before and after this line
print("Oil.......%8s"% oilPriceStr)    #using %8s so we can keep the right-most number
                                       #in the cost to stay 8 spaces from the text descriptor
                                       #that sticks the furthese out, and also to keep the all the
                                       #right-most numbers in the same column.
                                        
                                    
if (quartNum > 6): #-------------------------checking for volume discount
    print("Discount..%8.2f"% discountAmount)
if (oilFilter == 'Y'): #---------------------checking if filter price is included
    print("Filter....%8.2f"% filterPrice)
print("Service...%8.2f"% serviceFee)
print("%18s"% addLine) #------------- the dotted line separator is 18 spaces from the left-hand side of the window
print("Subtotal..%8.2f"% subtotal)
print("Tax.......%8.2f"% taxAmount)
print("%18s"% addLine)
print("Total.....%8s\n"% totalStr)
if (quartNum > 10): #----------------------checking if need to print EPA statement
    print(epaNotice)
    


