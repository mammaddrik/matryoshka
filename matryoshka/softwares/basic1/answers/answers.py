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
    "test whether a number is within 100 of 1000 or 2000."
    return ((abs(1000 -n) <= 100) or (abs(2000 -n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))""")
    
    #::::: Answer 18 :::::
    elif (sel == 18):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def sum_thrice(x, y, z):
    "The sum of three numbers."
    sum = x+y+z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))""")

    #::::: Answer 19 :::::
    elif (sel == 19):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def larger_string(str, n):
    "Is a repeater"
    result = ""
    for i in range(n):
        result = result + str
    return result
print(larger_string('abc',2))
print(larger_string('.py',3))""")

    #::::: Answer 20 :::::
    elif (sel == 20):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def new_string(str):
    "Function to check if there is or not."
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str
print(new_string(" Array"))
print(new_string("Is Empty"))""")
    
    #::::: Answer 21 :::::
    elif (sel == 21):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")""")
            
    #::::: Answer 22 :::::
    elif (sel == 22):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(list_count_4([1, 4, 6, 7, 4]))""")
            
    #::::: Answer 23 :::::
    elif (sel == 23):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def substring_copy(str, n):
    "A function to get n (a non-negative integer)"
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]
    
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(substring_copy("abcdef", 2))""")
            
    #::::: Answer 24 :::::
    elif (sel == 24):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def is_vowel(char):
    "A function to check vowels"
    all_vowels = "aeiou"
    return char in all_vowels
print(is_vowel("c"))""")
     
    #::::: Answer 25 :::::
    elif (sel == 25):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def is_group_member(group_data, n):
    "A function to check if number exists."
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))""")

    #::::: Answer 26 :::::
    elif (sel == 26):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def histogram(items):
    "A function to make a histogram."
    for n in items:
        output = ""
        times = n
        while(times > 0):
            output += "*"
            times = times - 1
        print(output)
histogram([2, 3, 6, 5])""")

    #::::: Answer 27 :::::
    elif (sel == 27):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def concatenate_list_data(list):
    "A function for concatenation."
    result = ""
    for element in list:
        result += str(element)
    return result
print(concatenate_list_data([1, 5 ,12 ,2]))""")

    #::::: Answer 28 :::::
    elif (sel == 28):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))""")
            
    #::::: Answer 29 :::::
    elif (sel == 29):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""b = int(input("Input the base: "))
h = int(input("Input the height: "))
area = b*h/2
print(f"area = {area}")""")
            
    #::::: Answer 30 :::::
    elif (sel == 30):
        if (option.upper() == "Y"):
            print("\nAnswer:\n")
            print(r"""def gcd(x, y):
    "The function to calculate the greatest common divisor."
    gcd = 1
    if (x % y == 0):
        return y
    for k in range(int(y / 2), 0 , -1):
        if (x % k == 0 and y % k == 0):
            gcd = k
            break
    return gcd
print(gcd(12, 17))""")