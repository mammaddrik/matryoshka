#!/usr/bin/env python
#
#                  _                        _     _         
#                 | |                      | |   | |        
#  _ __ ___   __ _| |_ _ __ _   _  ___  ___| |__ | | ____ _ 
# | '_ ` _ \ / _` | __| '__| | | |/ _ \/ __| '_ \| |/ / _` |
# | | | | | | (_| | |_| |  | |_| | (_) \__ \ | | |   < (_| |
# |_| |_| |_|\__,_|\__|_|   \__, |\___/|___/_| |_|_|\_\__,_|
#                            __/ |                          
#                           |___/     
#     
#              My Python Examples for Everyone                    
#                    Github: mammaddrik       

#::::: Softwares :::::
from matryoshka.softwares.array import array
from matryoshka.softwares.basic1.basic1 import basic1
from matryoshka.softwares.basic2 import basic2
from matryoshka.softwares.basic3 import basic3
from matryoshka.softwares.collection import collection
from matryoshka.softwares.conditionalstatement import conditionalstatement
from matryoshka.softwares.csv import csv
from matryoshka.softwares.datastructure import datastructure
from matryoshka.softwares.datatime import datatime
from matryoshka.softwares.File import File
from matryoshka.softwares.function import function
from matryoshka.softwares.github import github
from matryoshka.softwares.heapqueue import heapqueue
from matryoshka.softwares.json import json
from matryoshka.softwares.Lambda import Lambda
from matryoshka.softwares.linkedlist import linkedlist
from matryoshka.softwares.List import List
from matryoshka.softwares.maths import maths
from matryoshka.softwares.oops import oops
from matryoshka.softwares.os import os
from matryoshka.softwares.pattern import pattern
from matryoshka.softwares.re import re
from matryoshka.softwares.recurion import recurion
from matryoshka.softwares.searchsort import searchsort
from matryoshka.softwares.sqlite import sqlite
from matryoshka.softwares.string import string
from matryoshka.softwares.Tuple import Tuple

#::::: Library :::::
from matryoshka.library.clearscreen.clearscr import clearScr
from matryoshka.library.color.color import Color,color_banner
from matryoshka.library.slowprint.slowprint import slowprint
from matryoshka.library.banner.banner import Banner

#::::: Default Library :::::
import sys
import time
import os

#::::: Again :::::
def again():
    """A Function To Ask The User To Restart The Program."""
    matryoshka_again = input(Color.BCyan+"""\n    Do You Want To Continue?"""+Color.End+"""\n\t┌───(matryoshka)─[~/again]─[Y/n]
\t└─"""+color_banner[0]+"""$ """+Color.End)
    if (matryoshka_again.upper() == "Y" or matryoshka_again == ""):
        clearScr()
        time.sleep(0.4)
        matryoshka()
    elif (matryoshka_again.upper() == "N"):
        print("\n\tGoodbye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    else:
        clearScr()
        matryoshka()

#::::: matryoshka :::::
def matryoshka():
    """The Main Function Of Matryoshka, The First Page Of The Program."""
    clearScr()
    time.sleep(0.4)
    print(Banner.matryoshka_banner)
    choice = input("""
┌───(matryoshka)─[~/matryoshka]
└─"""+color_banner[0]+"""$ """+Color.End)
    
    #::::: Basic1 :::::
    if (choice == "01" or choice == "1"):
        clearScr()
        time.sleep(0.4)
        print(Banner.basic1_banner)
        select = input("""
┌───(matryoshka)─[~/matryoshka/basic1]
└─"""+color_banner[1]+"""$ """+Color.End)
        
        if (select == "01" or select == "1"):
            basic1(select)
        elif (select == "02" or select == "2"):
            basic1(select)
        elif (select == "03" or select == "3"):
            basic1(select)
        elif (select == "04" or select == "4"):
            basic1(select)
        elif (select == "05" or select == "5"):
            basic1(select)
        elif (select == "06" or select == "6"):
            basic1(select)
        elif (select == "07" or select == "7"):
            basic1(select)
        elif (select == "08" or select == "8"):
            basic1(select)
        elif (select == "09" or select == "9"):
            basic1(select)
        elif (select == "10"):
            basic1(select)
        elif (select == "11"):
            basic1(select)
        elif (select == "12"):
            basic1(select)
        elif (select == "13"):
            basic1(select)
        elif (select == "14"):
            basic1(select)            
        elif (select == "15"):
            basic1(select)            
        elif (select == "16"):
            basic1(select)            
        elif (select == "17"):
            basic1(select)            
        elif (select == "18"):
            basic1(select)            
        elif (select == "19"):
            basic1(select)            
        elif (select == "20"):
            basic1(select)            
        elif (select == "21"):
            basic1(select)             
        elif (select == "22"):
            basic1(select)             
        elif (select == "23"):
            basic1(select)             
        elif (select == "24"):
            basic1(select)             
        elif (select == "25"):
            basic1(select)             
        elif (select == "26"):
            basic1(select)             
        elif (select == "27"):
            basic1(select)             
        elif (select == "28"):
            basic1(select)             
        elif (select == "29"):
            basic1(select)             
        elif (select == "30"):
            basic1(select)             
        elif (select == "31"):
            basic1(select)             
        elif (select == "32"):
            basic1(select)             
        elif (select == "33"):
            basic1(select)             
        elif (select == "34"):
            basic1(select)             
        elif (select == "35"):
            basic1(select)             
        elif (select == "36"):
            basic1(select)             
        elif (select == "37"):
            basic1(select)             
        elif (select == "38"):
            basic1(select)             
        elif (select == "39"):
            basic1(select)             
        elif (select == "40"):
            basic1(select)             
        elif (select == "41"):
            basic1(select)             
        elif (select == "42"):
            basic1(select)             
        elif (select == "43"):
            basic1(select)             
        elif (select == "44"):
            basic1(select)             
        elif (select == "45"):
            basic1(select) 
        elif (select == "46"):
            basic1(select) 
        elif (select == "47"):
            basic1(select) 
        elif (select == "48"):
            basic1(select) 
        elif (select == "49"):
            basic1(select) 
        elif (select == "50"):
            basic1(select) 
        elif (select == "51"):
            basic1(select) 
        elif (select == "52"):
            basic1(select) 
        elif (select == "53"):
            basic1(select) 
        elif (select == "54"):
            basic1(select) 
        elif (select == "55"):
            basic1(select) 
        elif (select == "56"):
            basic1(select) 
        elif (select == "57"):
            basic1(select) 
        elif (select == "58"):
            basic1(select) 
        elif (select == "59"):
            basic1(select) 
        elif (select == "60"):
            basic1(select) 
        elif (select == "61"):
            basic1(select) 
        elif (select == "62"):
            basic1(select) 
        elif (select == "63"):
            basic1(select) 
        elif (select == "64"):
            basic1(select) 
        elif (select == "65"):
            basic1(select) 
        elif (select == "66"):
            basic1(select) 
        elif (select == "67"):
            basic1(select) 
        elif (select == "68"):
            basic1(select) 
        elif (select == "69"):
            basic1(select) 
        elif (select == "70"):
            basic1(select) 
        elif (select == "71"):
            basic1(select) 
        elif (select == "72"):
            basic1(select) 
        elif (select == "73"):
            basic1(select) 
        elif (select == "74"):
            basic1(select) 
        elif (select == "75"):
            basic1(select) 
        elif (select == "76"):
            basic1(select) 
        elif (select == "77"):
            basic1(select) 
        elif (select == "78"):
            basic1(select) 
        elif (select == "79"):
            basic1(select) 
        elif (select == "80"):
            basic1(select) 
        elif (select == "81"):
            basic1(select) 
        elif (select == "82"):
            basic1(select) 
        elif (select == "83"):
            basic1(select) 
        elif (select == "84"):
            basic1(select) 
        elif (select == "85"):
            basic1(select) 
        elif (select == "86"):
            basic1(select) 
        elif (select == "87"):
            basic1(select) 
        elif (select == "88"):
            basic1(select) 
        elif (select == "89"):
            basic1(select) 
        elif (select == "90"):
            basic1(select) 
        elif (select == "91"):
            basic1(select) 
        elif (select == "92"):
            basic1(select) 
        elif (select == "93"):
            basic1(select) 
        elif (select == "94"):
            basic1(select)
        elif (select == "95"):
            basic1(select) 
        elif (select == "96"):
            basic1(select)
        elif (select == "97"):
            basic1(select)
        elif (select == "98"):
            basic1(select) 
        elif (select == "99"):
            basic1(select) 
        elif (select == "100"):
            basic1(select)                          
        elif (select == "00" or select == "0"):
            matryoshka()
        else:
            again()
            
        matryoshka()
    
    elif (choice == "02" or choice == "2"):
        pass

    elif (choice == "03" or choice == "3"):
        pass

    elif (choice == "04" or choice == "4"):
        pass

    elif (choice == "05" or choice == "5"):
        pass

    elif (choice == "06" or choice == "6"):
        pass

    elif (choice == "07" or choice == "7"):
        pass

    elif (choice == "08" or choice == "8"):
        pass

    elif (choice == "09" or choice == "9"):
        pass

    elif (choice == "10"):
        pass

    elif (choice == "11"):
        pass

    elif (choice == "12"):
        pass

    elif (choice == "13"):
        pass

    elif (choice == "14"):
        pass

    elif (choice == "15"):
        pass

    elif (choice == "16"):
        pass

    elif (choice == "17"):
        pass

    elif (choice == "18"):
        pass
    
    elif (choice == "19"):
        pass    
    
    elif (choice == "20"):
        pass    
    
    elif (choice == "21"):
        pass    
    
    elif (choice == "22"):
        pass    
    
    elif (choice == "23"):
        pass    
    
    elif (choice == "24"):
        pass    
    
    elif (choice == "25"):
        pass    
    
    elif (choice == "26"):
        pass    
    
    elif (choice == "00" or choice == "0"):
        clearScr()
        print(Banner.github_banner)
    
    elif (choice == "99"):
        print("\nGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
           
    again()
try:
    matryoshka()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4) 
    clearScr()
    sys.exit() 