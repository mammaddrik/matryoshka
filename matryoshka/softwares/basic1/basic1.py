#
#   _               _     __ 
#  | |             (_)   /_ |
#  | |__   __ _ ___ _  ___| |
#  | '_ \ / _` / __| |/ __| |
#  | |_) | (_| \__ \ | (__| |
#  |_.__/ \__,_|___/_|\___|_|                       

#::::: Answers :::::
from matryoshka.softwares.basic1.answers.answers import answer

#::::: Library :::::
from matryoshka.library.clearscreen.clearscr import clearScr
from matryoshka.library.color.color import Color,color_banner
from matryoshka.library.slowprint.slowprint import slowprint
from matryoshka.library.banner.banner import Banner

#::::: Back :::::
def back():
    "A Function To Execute The Questions Of This Program."
    back = input(Color.BCyan+"""\n    You Want To Go Back One Step Before?"""+Color.End+"""\n\t┌───(matryoshka)─[~/back]─[Y/n]
\t└─"""+color_banner[1]+"""$ """+Color.End)
    if (back.upper() == "Y" or back == ""):
        clearScr()
        print(Banner.basic1_banner)
        select = input("""
┌───(matryoshka)─[~/matryoshka/basic1]
└─"""+color_banner[1]+"""$ """+Color.End)
        basic1(select)
    else:
        pass

def basic1(select):
    "The Main Function Of Basic1."
    #::::: Question 1 :::::
    if (select == "01" or select == "1"):
        clearScr()
        slowprint("""Write a Python program to print the following 
string in specific formar (see the output).""")
        output = ("""\nOutput:
Twinkle, twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!""")
        print(output)
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(1,option)
        back()
    
    #::::: Question 2 :::::
    elif (select == "02" or select == "2"):
        clearScr()
        slowprint("""Write a Python program to get the Python 
version and version info you are using.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(2,option)
        back()
    
    #::::: Question 3 :::::
    elif (select == "03" or select == "3"):
        clearScr()
        slowprint("""Write a Python program to display the current 
data and time. """+Color.BRed+"""[12-Hour Clock]"""+Color.End)
        output = ("\nOutput:\nYear-Month-Day Hour:Minutes:Seconds")
        print(output)
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(3,option)
        back()
        
    #::::: Question 4 :::::
    elif (select == "04" or select == "4"):
        clearScr()
        slowprint("""Write a Python program which accepts the redius
of a circle from the user and compute the area.""")        
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(4,option)
        back()
        
    #::::: Question 5 :::::
    elif (select == "05" or select == "5"):
        clearScr()
        slowprint("""Write a Python program which accepts the user's 
first and last name and print then in reverse order
whith a space between them.""")      
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(5,option)
        back()

    #::::: Question 6 :::::
    elif (select == "06" or select == "6"):
        clearScr()
        slowprint("""Write a Python program which accepts a sequence
of comma-separated number from user and generate 
a list and a tuple with those number.""")
        output = ("\nSample data: 3,5,7,23")
        print(output) 
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(6,option)
        back()
        
    #::::: Question 7 :::::
    elif (select == "07" or select == "7"):
        clearScr()
        slowprint("""Write a Python program which accepts a filename
from the user and print the extension of that.""")    
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(7,option)
        back()

    #::::: Question 8 :::::
    elif (select == "08" or select == "8"):
        clearScr()
        slowprint("""Write a Python program to display the first and last
colors from the follwing list.""")
        output = ("\ncolor_list = [Red,Green,White,Black]")
        print(output)      
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(8,option)
        back()
        
    #::::: Question 9 :::::
    elif (select == "09" or select == "9"):
        clearScr()
        slowprint("""Write a Python program to display the examination
schedule. (extract the date from exam_st_date)""")
        output = ("\nexam_st_data = (1,31,2023)")
        print(output)       
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(9,option)
        back()
        
    #::::: Question 11 :::::
    elif (select == "11"):
        clearScr()
        slowprint("""Write a Python program to print the documents
(syntax, description etc.) of Python built-in function(s).""")
        output = ("\nSample function:abs()")
        print(output)    
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(11,option)
        back()

    #::::: Question 12 :::::
    elif (select == "12"):
        clearScr()
        slowprint("""Write a Python program to print the calendar
of a given month and year.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(12,option)
        back()

    #::::: Question 13 :::::
    elif (select == "13"):
        clearScr()
        slowprint("""Write a Python program to print the following 
'here document'. """+Color.BRed+"""[multi-line]"""+Color.End)
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(13,option)
        back()
        
    #::::: Question 14 :::::
    elif (select == "14"):
        clearScr()
        slowprint("""Write a Python program to calculate number of 
days between two dates.""")
        output = ("""\n2014,7,2
2014,7,11""")
        print(output)
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(14,option)
        back()
    
    #::::: Question 15 :::::
    elif (select == "15"):
        clearScr()
        slowprint("""Write a Python program to get the volume of a 
sphere with radius 6.""")
        output = ("\npi = 3.1415926535897931")
        print(output)
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(15,option)
        back()
    
    #::::: Question 16 :::::
    elif (select == "16"):
        clearScr()
        slowprint("""Write a Python program to get the difference
between a given number and 17, if the number is greater 
than 17 return double the absolute difference.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(16,option)
        back()
    
    #::::: Question 17 :::::
    elif (select == "17"):
        clearScr()
        slowprint("""Write a Python program to test whether a number 
is within 100 of 1000 or 2000.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(17,option)
        back()

    #::::: Question 18 :::::
    elif (select == "18"):
        clearScr()
        slowprint("""Write a Python program to calculate the sum of
three given number, if the values are equal 
then return thrice of their sum.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(18,option)
        back()

    #::::: Question 19 :::::
    elif (select == "19"):
        clearScr()
        slowprint("""Write a Python program to get a string 
which is n (non-negative integer) copies of a given str.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(19,option)
        back()

    #::::: Question 20 :::::
    elif (select == "20"):
        clearScr()
        slowprint("""Write a Python program to get a new string from 
a given string where 'Is' has been added to the front.
if the give string already begins whith 'Is' 
then return the string unchanged.""")
        option = input(Color.BCyan+"""
Do you want to see the answer?"""+Color.End+"""
┌───(matryoshka)─[~/answer]─[y/N]
└─"""+color_banner[1]+"""$ """+Color.End)
        answer(20,option)
        back()