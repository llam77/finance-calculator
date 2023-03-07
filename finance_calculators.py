# This is a program 

# User choose from investment or bond to calculate the investment return or monthly repay


import math

# user enter "investment" or "bond" calculator

selection = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment  -   to calculate the amount of interest you'll earn on your investment
bond        -   to calculate the amount you'll have to pay on a home loan

Input: """)

print()

# make sure capitalises won't affacted 

selection = selection.lower()

# investment calculator

if selection == "investment":

    # get user input for investment

    print("Investment calculator selected! Please input the following details\n")
    inv_deposit = float(input("{:<40}".format("deposit amount:")))
    inv_rate = float(input("{:<40}".format("interest rate:")))
    inv_year = float(input("{:<40}".format("years to invest:")))
    inv_interest = input("{:<40}".format("'simple' or 'compound' interest:"))
    
    # make sure capitalises won't affacted

    inv_interest = inv_interest.lower()

    # calculation for simple or compund interest

    if inv_interest == "simple":
        final_amount = round(inv_deposit * (1 + inv_rate / 100 * inv_year), 2)
    elif inv_interest == "compound":
        final_amount = round(inv_deposit * (1 + inv_rate / 100) ** inv_year, 2)

    print()
    
    # print out total return
    
    print("{:<40}{:.2f}\n".format("Total return (deposit + interest):", final_amount))

# bond caculator

elif selection == "bond":
    
    # get user input for bond
    
    print("Bond calculator selected! Please input the following details\n")
    bon_value = float(input("{:<40}".format("present value of house:")))
    bon_rate = float(input("{:<40}".format("interest rate:")))
    bon_month = int(input("{:<40}".format("months to repay bond:")))

    # calculate monthly payment for bond
    
    bon_repay = round(((bon_rate / 100) * bon_value) / (1 - (1 + (bon_rate / 100)) ** (-bon_month)), 2)

    print()

    # print out monthly repayment

    print("{:<40}{:.2f}\n".format("Monthly repayment of bond:", bon_repay))