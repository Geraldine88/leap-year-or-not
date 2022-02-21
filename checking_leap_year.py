"""
A year is a Leap Year if it is exactly divisible by 4, except for century years (years ending with 00).
A century year is, however, a Leap year if it is divisible by 400.
Any other year is NOT a leap year

Refer to the multiples of 4 or 400
"""



your_year = int(input("Enter the year you wish to check: "))

#If the year is a century year and is diivisible by 400, it is a leap year
if ( your_year %400 == 0 ):
    print("%d is a Leap Year" %your_year)

#If the year is just simply divisible by 100, it is a century year but not a leap year
elif ( your_year %100 == 0 ):
    print("%d is NOT a Leap Year" %your_year)

#If the year is divisible by 4, it satisfies the condition of a leap year
elif ( your_year %4 == 0 ):
    print("%d is a Leap Year" %your_year)

#Else, any other year does not satisfy the condition of being a leap year
else:
    print ("%d is NOT a Leap Year" %your_year)

