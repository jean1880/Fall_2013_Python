"""
Assignment 3 - Ordering program
Coded By: Jean-Luc Desroches
Date: 11/28/12

Purpose: This program is designed to take input from a user
to put together a food order of burgers, drinks and fries,
with a maximum of 20 of any 1 item
"""
#Begin program and try catch for major system error
try:
    #import system modules
    import sys
    # Declare constant of food cost used between modules as global constants
    
    #Float Constant HAMBURGER_COST = 0.99
    #Float Constant FRY_COST = 0.79
    #Float Constant SODA_COST = 1.09
    
    # Set value of Constants
    HAMBURGER_COST = 0.99
    FRY_COST = 0.79
    SODA_COST = 1.09

    ############ Retrieve Order Number #########################

    def getOrderNumber():
        #Boolean leave
        #Integer orderNumber
        #Integer Constant MIN_NUM = 0
        MIN_NUM = 0
        leave=False
        
        while(not leave):
            print("--------------ORDER NUMBER---------------")
            print("")
            try:
                orderNumber=int(input("Please enter the order number: "))
                print("")
                if(orderNumber >= MIN_NUM):
                    return orderNumber
                else:
                    print("Please ennter a number greater than 0")
            except(ValueError):
                print("")
                print("Error order must be a numeric sequence \ngreater than 0")
                print("")

    #############################################################

    ####################### Show Menu ###########################

    def showMenu(orderNumber):
        #String item, exitPrompt, itemName
        #Integer burgerCount, fryCount, sodaCount
        #Float burgerCost, fryCost, sodaCost, taxCost, subTotal, total
        #Boolean leave, checkExit
        
        #Initialize all order values to 0
        burgerCount=burgerCost=fryCount=fryCost=sodaCount=sodaCost=0
        
        #initialize exit command to false
        leave=False
        
        while(not leave):
            try:
                print("------------------MENU--------------------")
                print("-------------\t %d \t-------------" %orderNumber)
                print("")
                print("Please select a menu item the customer \n wishes to purchase. Select option 5 \n to exit and cancel purchase")
                print("")
                print("------------------------------------------")
                print("1. Yum Yum Burgers \t= $0.99")
                print("2. Grease Yum Fries \t= $0.79")
                print("3. Soda Yums \t\t= $1.09")
                print("4. Print Receipt")
                print("5. Exit")
                print("------------------------------------------")
                print("")
                item = int(input("Please select a menu item by entering the \nmatching number: "))
                print("")

                # option 1, get the number of hamburgers the customer wishes to order
                if(item == 1):
                    itemName = "Yum Yum Burgers"
                    burgerCount=getItem(itemName,burgerCount)
                    burgerCost=calculateItemCost(itemName,burgerCount)

                # option 2, get the number of fries the customer wishes to order
                elif(item == 2):
                    itemName = "Grease Yum Fries"
                    fryCount=getItem(itemName,fryCount)
                    fryCost=calculateItemCost(itemName, fryCount)

                # option 3, get the number of sodas the customer wishes to order
                elif(item == 3):
                    itemName="Soda Yums"
                    sodaCount=getItem(itemName,sodaCount)
                    sodaCost=calculateItemCost(itemName,sodaCount)

                # option 4, calculate totals and print a reciept on the screen for the user
                elif(item == 4):
                    subTotal=calculateTotalCost(burgerCost,fryCost,sodaCost)
                    taxCost=calculateTax(subTotal)
                    total=calculateFinalCost(subTotal,taxCost)
                    printAll(burgerCount,fryCount, sodaCount, burgerCost, fryCost, sodaCost, subTotal, taxCost, total, orderNumber)
                    return

                # option 5, check if user wishes to cancel the order
                elif(item == 5):
                    checkExit=False
                    while(not checkExit):                  
                        exitPrompt = input("Are you sure you wish to exit and cancel \nthe order?(y/n) ")
                        print("")
                        if(exitPrompt=="y" or checkExit=="Y"):
                            leave = True
                            checkExit=True
                            return
                        elif(exitPrompt!="n" and checkExit!="N"):
                            print("")
                            print("------------------------------------------")
                            print("Command not recognized, please enter y/Y \nfor yes or n/N for no")
                            print("------------------------------------------")
                            print("")
                        else:
                             checkExit=True

                # Display error message on any other numeric input
                else:
                    print("")
                    print("------------------------------------------")
                    print("Command not recognized, please choose \nan item from the menu above")
                    print("------------------------------------------")
                    print("")

            # print an error message if user inputs non-numeric value
            except(ValueError):
                print("")
                print("------------------------------------------")
                print("You entered a non numeric value, please \nenter a numeric value")
                print("------------------------------------------")
                print("")

    #############################################################

    ################# Get item count ############################

    def getItem(itemName,itemCount):
        #Integer itemCount, orderCount, canOrderTheseMany
        #Integer Constant MAX_ORDER = 20
        #Integer Constant MIN_ORDER = 0
        MAX_ORDER=20
        MIN_ORDER=0

        # calculate how many of the item can still be ordered
        canOrderTheseMany = MAX_ORDER - itemCount

        # initialize leave variable and get user input
        leave=False
        print("------------------------------------------")
        print("")
        print("-------\t%s\t-------" %itemName)
        print("")
        print("Number of %s currently on order:" %itemName)
        print("")
        while(not leave):
            try:
                print("%s : %d"%( itemName, itemCount))
                print("")
                print("==========================================")
                print("")
                print("Can order %d more %s" %(canOrderTheseMany, itemName))
                print("")
                print("------------------------------------------")
                orderCount = int(input("Please enter the number of %s the \ncustomer wishes to order. To remove items \nplease enter a negative value: "%itemName))
                print("")
                # check input, see if it will make order count less or greater than maximums allowed
                if ((canOrderTheseMany-orderCount)<MIN_ORDER):
                    print("------------------------------------------")
                    print("That is more than the customer can order")
                    print("------------------------------------------")
                    print("")
                elif((orderCount+itemCount)<MIN_ORDER):
                    print("------------------------------------------")
                    print("That is less than the customer can order")
                    print("------------------------------------------")
                    print("")
                else:
                    itemCount = itemCount + orderCount
                    return itemCount

            # Display error message on non-numeric input
            except(ValueError):
                print("")
                print("You entered a non-numeric entry, please \n enter a proper value in numeric format to continue")
                print("")
                print("------------------------------------------")
                print("")

    ############################################################

    ############### Calculate Item Cost ########################

    def calculateItemCost(itemName, number_of_item):
        #string itemName
        #integer number_of_item
        #Float totalCost



        # based on item name, calculate cost of the item
        if(itemName=="Yum Yum Burgers"):
           cost = number_of_item * HAMBURGER_COST
        elif(itemName=="Grease Yum Fries"):
           cost = number_of_item * FRY_COST
        elif(itemName=="Soda Yums"):
           cost = number_of_item * SODA_COST
        return cost

    ###########################################################

    ############## Calculate the subtotal Cost #################

    def calculateTotalCost(burgerCost,fryCost,sodaCost):
        total = burgerCost+fryCost+sodaCost
        return total

    ###########################################################

    ################## Calculate Tax ##########################

    def calculateTax(totalCost):
        #Float Constant TAX=1.13
        TAX=1.13
        return(totalCost*TAX)

    ###########################################################

    ################## Calculate Final Price ##################

    def calculateFinalCost(subTotal,taxCost):
        #float finalCost
        finalCost = subTotal+taxCost
        return finalCost

    ##########################################################

    ############### Print out Receipt on screen ##############

    def printAll(burgerCount,fryCount, sodaCount, burgerCost, fryCost, sodaCost, subTotal, taxCost, total, orderNumber):
        print("----------------RECIEPT-------------------")
        print("--------\t %d \t--------"%orderNumber)
        print("==========================================")
        print("")
        print("Yum Yum Burgers:\t %d @ $%.2f = $%.2f"%(burgerCount, HAMBURGER_COST, burgerCost))
        print("Grease Yum Fries:\t %d @ $%.2f = $%.2f"%(fryCount, FRY_COST, fryCost))
        print("Soda Yums:\t\t %d @ $%.2f = $%.2f"%(sodaCount, SODA_COST, sodaCost))
        print("")
        print("------------------------------------------")
        print("Subtotal: \t\t $%.2f" %subTotal)
        print("Tax: \t\t\t $%.2f" %taxCost)
        print("__________________________________________")
        print("Total: \t\t\t $%.2f" %total)
        print("")
        return

    ##########################################################

    ################### Main module ##########################

    def main():
        #Integer orderNumber
        #Boolean exitCheck

        #Initialize Variables

        exitCheck = False
        
        try:
            # Initialise main program loop
            while(True):
                orderNumber = getOrderNumber()
                showMenu(orderNumber)
                print("------------------------------------------")
                print("")
                # check if user wishes to enter another order
                while(not exitCheck):
                    exitPrompt=input("Do you wish to enter an Order?(y/n): ")
                    print("")
                    if(exitPrompt == "n" or exitPrompt == "N"):
                        sys.exit()                        
                    if(exitPrompt != "y" and exitPrompt != "Y"):
                       print("Command not recognized, please input either y/Y \n to exit program or n/N to continue")
                    else:
                        exitCheck=True
                           
        # print friendly exit output on program exit
        except(SystemExit):
            print("")
            print("------------------------------------------")
            print("Program terminated \nThank you, have a good day")
            print("------------------------------------------")
                    
    #########################################################

    main()



except(Exception):
    print("ERROR!")
    print("PROGRAM HAS EXPERIENCED A FATAL ERROR \nTERMINATING")
