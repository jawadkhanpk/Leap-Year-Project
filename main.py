# How leap year works
# every year that is evenly divisible by 4
# except every yeat that is evenly divisible by 100
# unless the year  is also evenly  divisible by 400

year = int(input("Which year do you want to check? \n"))

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("it is leap year")
        else:
            print("it is not a leap year")
    else:
        print("It is leap year")
else:
    print("Not a leap year")