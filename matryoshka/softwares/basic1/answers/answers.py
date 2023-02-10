def answer(sel,option):
    "A Function To Specify The Answer To Each Question."
    #::::: Answer 1 :::::
    if (sel == 1):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"print(Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \nHow I wonder what you are!)")
    
    #::::: Answer 2 :::::
    elif (sel == 2):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""import sys
version = sys.version
info = sys.version_info
print(f"Python Version is: {version}")
print(f"Version Info is: {info}")""")
    
    #::::: Answer 3 :::::
    elif (sel == 3):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""import datetime
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%I:%M:%S %p")
print(f"Current date and time: {date}  {time}")""")
            
    #::::: Answer 4 :::::
    elif (sel == 4):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""from math import pi
radius = float(input("Input the radius of the circle: "))
area = round(pi * radius ** 2,2)
print(f"The area of the circle with radius {str(radius)} is: {str(area)}")""")
            
    #::::: Answer 5 :::::
    elif (sel == 5):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""fname = input("Input your First Name: ")
lname = input("Input your Last Name: ")
print(f"{lname} {fname}")""")
    
    #::::: Answer 6 :::::
    elif (sel == 6):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""values = input("Input some comma-seprated number: ")
create_list = values.split(",")
create_tuple = tuple(create_list)
print(f"List: {create_list}")
print(f"Tuple: {create_tuple}")""")
            
    #::::: Answer 7 :::::
    elif (sel == 7):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""filename = input("Input the Filename: ")
f_extns = filename.split(".")
f_extns = repr(f_extns[-1])
print(f"The extension of the file is: {f_extns}")""")
    
    #::::: Answer 8 :::::
    elif (sel == 8):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""color_list = ["Red","Green","White","Black"]
print(f"{color_list[0]} {color_list[-1]}")""")
    
    #::::: Answer 9 :::::
    elif (sel == 9):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""exam_st_data = (1,31,2023)
print(f"The examination will start from: {exam_st_data[0]}/{exam_st_data[1]}/{exam_st_data[2]}")""")
    
    #::::: Answer 10 :::::
    elif (sel == 10):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""n = int(input("Input a number n: "))
a = str(n)
n2 = a + a
n3 = a + a + a
result = n + int(n2) + int(n3)
print(f"The value is: {result}")""")
            
    #::::: Answer 11 :::::
    elif (sel == 11):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"print(abs.__doc__)")
    
    #::::: Answer 12 :::::
    elif (sel == 12):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""import calendar
year = int(input("Input the year: "))
month = int(input("Input the month: "))
print(calendar.month(year,month))""")
    
    #::::: Answer 13 :::::
    elif (sel == 12):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""print('''
a string than you "don't" have to escape
This
ia a ....... multi-line
heredoc string -------> example''')""")
                         
    #::::: Answer 14 :::::
    elif (sel == 14):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)""")
            
    #::::: Answer 15 :::::
    elif (sel == 15):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)""")
    
    #::::: Answer 16 :::::
    elif (sel == 16):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
        print(r"""def difference(n):
    "Difference Between A Given Number And 17."
    if n <= 17:
        return 17 - n
    else:
        return (n -17) * 2
print(difference(22))
print(difference(14))""")
    
    #::::: Answer 17 :::::
    elif (sel == 17):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def near_thousand(n):
    return ((abs(1000 -n) <= 100) or (abs(2000 -n) <= 100))
    
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))""")