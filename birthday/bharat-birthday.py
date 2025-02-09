# %%
# Name: how_old
# Purpose: to calculate the age of a person based on the person's date of birth
# Inputs:   1. user inputted year as int
#           2. user inputted month as int
#           3. user inputted day as int
# Outputs:  1. int of the age of a person
# Side effects: none

import datetime as dt

def how_old():
    print("How old are you??")
    user_year = int(input("Enter 4 digits for your birth year: ")) # user enters birth year
    user_month = int(input("Enter 2 digits for your birth month: ")) # user enters birth month
    user_day = int(input("Enter 2 digits for your birth day: ")) # user enters birth day

    timedelta_from_birth = dt.date.today() - dt.date(user_year, user_month, user_day) # calculate timedelta from birth to today
    days_from_birth = timedelta_from_birth.days # get days since birth
    age = days_from_birth // 365 # floor divide by number of days in a year to get number of years aka age
    return age

how_old()



