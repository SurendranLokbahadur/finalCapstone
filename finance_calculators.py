import math

print()
print("The financial calculator options are")
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print()
print("bond - to calculate the amount you'll have to pay on a home loan")
print()
print()
option_chosen = input("Enter either 'investment' or 'bond' from the menu above to start:")
print()

# PART 1 - BASED ON CHOSEN OPTION GETTING THE INPUT FOR INVESTMENT
if(option_chosen == "investment" or option_chosen == "Investment" or option_chosen == "INVESTMENT"):
    money_deposit_p = int(input("Enter the amount of money that you want to deposit: "))
    print()
    interest_rate_r = int(input("Enter the interest rate for your deposit only the numbers: "))
    print()
    number_of_years_t = int(input("Enter the number of years for your deposit: "))
    print()
    interest_type = input("Do you want to proceed with 'simple' or 'compound' interest:")
    print()

# CALCULATING SIMPLE INTEREST AND ADDING IT WITH ORIGINAL INVESTMENT AMOUNT
    # A = P*(1 + r*t)
    if(interest_type == "simple" or interest_type == "Simple" or interest_type =="SIMPLE"):

        total_amount_after_interest_A = money_deposit_p * (1+ interest_rate_r * number_of_years_t)
        total_amount_after_interest_percentage = total_amount_after_interest_A / 100
        final_amount_with_interest = total_amount_after_interest_percentage + money_deposit_p
        print(" Your total amount after the interest applied is: "+ "£ " + str(final_amount_with_interest))
        print()
        
    # CALCULATING COMPOUND INTEREST AND ADDING IT WITH ORIGINAL INVESTMENT AMOUNT
    # A = P * math.pow((1+r),t)
    elif(interest_type == "compound" or interest_type == "Compound" or interest_type =="COMPOUND"):

        total_amount_after_interest_A = money_deposit_p * math.pow ((1+ interest_rate_r) , number_of_years_t)
        total_amount_after_interest_percentage = total_amount_after_interest_A / 100000
        final_amount_with_interest = total_amount_after_interest_percentage + money_deposit_p
        print(" Your total amount after the interest applied is: "+ "£ " + str(final_amount_with_interest))
        print()


    else:
        print("you have chosen an option that is out of the list")


# PART 2 - BASED ON CHOSEN OPTION GETTING THE INPUT FOR BOND

elif(option_chosen == "bond" or option_chosen =="Bond" or option_chosen== "BOND"):
    print()
    present_value_P = float(input("Enter the present value of your house: "))
    print()
    number_of_months_n = int(input("Enter the number of months your bond will be repaid: "))
    print()
    interest_rate_i = int(input("Enter your monthly interest rate: "))
    interest_rate_ii = number_of_months_n /100
    interest_rate_iii = interest_rate_ii/12
    print()

# CALCULATING MONTHLY REPAYMENT TO REPAY THE BOND
    #repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment_r = (interest_rate_iii * present_value_P)/(1 - (1 + interest_rate_iii)**(-number_of_months_n))
    print()
    print("The money your have to repay for your bond in each month is:" + str(repayment_r))
    print()

else:
    print("you have chosen an option that is out of the list")
    print()
