"""
Assignment #4
Coded By: Jean-Luc Desroches
Date: Dec. 11/2012

Purpose: A program that will allow a user to enter the energy bills
from January to December for a year prior to having gone green.  Next,
it will allow the user to enter the energy bills from January to December
of the year after going green. The program then calculate the energy
savings by subtracting the cost prior to going green from the costs after
going green values. The energy bills and the savings are then displayed for
the two year’s worth of data.
"""
#Import sytem library
import time

#Declare global variables
#String MONTHS
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']





################### Main Module ########################

def main():
    #Declare local variables
    #Float yearBeforeGreen, yearAfterGreen, savingFromGreen
    #Boolean leave

    #Initialise variables
    leave=False
    yearBeforeGreen=[0]*12
    yearAfterGreen=[0]*12
    savingsFromGreen=[0]*12
    
    #Display welcome message to user and purpose of the program
    print_welcome_message()
    #Begin a master loop to allow user to enter data multiple times
    while leave != True:
        #Prime user
        print_input_message()
        print("===========================================")
        print("Please enter the data for energy costs during\nthe year prior to going Green")
        print("===========================================")
        print("")
        # call module to get data of year before going green
        get_year_of_data(yearBeforeGreen)
        print_input_message()
        print("===========================================")
        print("Please enter the data for enrgy costs during\nthe year after  going Green")
        print("===========================================")
        print("")
        # call module to get data of year after going green
        get_year_of_data(yearAfterGreen)
        # call module to calculate savings from going green
        savingsFromGreen=get_savings(yearBeforeGreen,yearAfterGreen)
        # call module to display results to the user
        display_results(yearBeforeGreen,yearAfterGreen,savingsFromGreen)
        # call module to get input from user whther to continue
        leave=query_continue()
        if(leave==True):
            try:
                raise SystemExit
            except(SystemExit):
                # call custom exit module
                sys_exit()
                    

################## END OF MAIN ##########################









############### Get year of Data ########################
# This module gets input from the user for the energy
# costs of each month

def get_year_of_data(yearCost):
    # Declare local variables
    # Boolean inputValid
    # Constant Float MIN_COST = 400
    # Constant Float MAX_COST = 1000
    MIN_COST = 400
    MAX_COST = 1000
    
    # Prep user with rules in data entry
    print("")
    print("===========================================")
    print("")
    print("Please enter the energy costs for the year,\ncosts must be between $400 - $1000. When\nentering costs please enter the numeric\nvalue only, ommiting the '$' sign")
    print("")
    print("===========================================")
    print("")

    # begin loop to cysle through months and get users input for Data
    for index in range(len(yearCost)):
        # Initialize inputValid to false to initiate loop
        inputValid = False
        while(inputValid == False):
            try:
                yearCost[index]=float(input("Please enter the costs for the month of \n%s: " %MONTHS[index]))
                if(yearCost[index]>=MIN_COST and yearCost[index]<=MAX_COST):
                    inputValid=True
                else:
                    print("")
                    print("------------------------------------------")
                    print("Error: Input must be greater than $%.2f and \nless than $%.2f" %(MIN_COST, MAX_COST))
                    print("------------------------------------------")
                    print("")
            except(ValueError):
                print("")
                print("------------------------------------------")
                print("Error: You have entered non-numeric information\n please enter the data using only numbers")
                print("------------------------------------------")
                print("")
    return(yearCost)

############### End of Data Module ######################









############# Calulate Savings Module ###################
# this module returns the difference between afterGreen
# and beforeGreen

def get_savings(yearBeforeGreen,yearAfterGreen):
    #Declare local variables
    # Float greenSavings
    greenSavings=[0]*12
    for index in range(len(yearBeforeGreen)):
        greenSavings[index]=yearBeforeGreen[index]-yearAfterGreen[index]
    return(greenSavings)


############# End of Savings Module ####################








############ Display Results Module ####################
# This Module displays the data in the arrays in a chart
# to the user

def display_results(yearBeforeGreen,yearAfterGreen,savingsFromGreen):
    # call module to display output message
    print_output_message()
    # Print results
    print("_________________SAVINGS___________________")
    print("Savings | Not Green | Gone Green | Month")
    print("___________________________________________")
    
    # loop through array and display results
    for index in range(len(yearBeforeGreen)):
        print(" $%.2f   $%.2f   $%.2f  %s" %(savingsFromGreen[index], yearBeforeGreen[index], yearAfterGreen[index], MONTHS[index]))
    print("")
    print("===========================================")

############ End of Display Module #####################









############# Leave Query Module #######################

def query_continue():
    # Boolean leave
    leave = False

    # prompt user whether to exit or continue
    while(leave==False):
        leaveQuery=input("Do you wish to enter data for another college?\nEnter 'y' or 'Y' to continue or, 'n' or 'N' to exit")
        if(leaveQuery.lower() == "y"):
            leave = True
            return leave
        if(leaveQuery.lower() != "n"):
            print("Error: Command not recognized")
        else:
            return leave

############## End Leave module ########################




############# Print input module #######################
# Print to screen input heading

def print_input_message():
    print("")
    print("===========================================")
    print("----------------- INPUT -------------------")
    print("===========================================")
    print("")

########################################################





############# Welcome Message module ##################
# print to screen welcome heading

def print_welcome_message():
    print("===========================================")
    print("---------------- WELCOME ------------------")
    print("===========================================")
    print("")
    print("""Purpose: A program that will allow a user
to enter the energy bills from January
to December for a year prior to having
gone green.  Next, it will allow the
user to enter the energy bills from
January to December of the year after
going green. The program then calculate
the energy savings by subtracting the
cost prior to going green from the
costs after going green values. The
energy bills and the savings are then
displayed for the two year’s worth of
data.""")
    print("")
    print("------------------------------------------")
    print("")


######################################################





############## Output message module ################
#Displays output header

def print_out_message():
    print("")
    print("===========================================")
    print("--------------- OUTPUT DATA ---------------")
    print("===========================================")
    print("")

######################################################



############# System Exit Module #####################
# Module exits program after displaying exit text to user

def sys_exit():
    print("==================== END ====================")
    print("Thank you for using the Green Savings program")
    # delay 1 second
    time.sleep(1)
    print("Program is now terminating")

############## End of exit module #####################

    

main()
