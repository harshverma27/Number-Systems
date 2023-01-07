# Importing All the neccasory files :-
from inttobin import *
from inttooct import *
from inttohex import *
from bintoint import *
from octtoint import *
from hextoint import * 
from colorama import * 

# Creating a class 'Number'
class number:

    # The class will have 4 basic parameters int,bin,oct and hexadecimal
    num = float()
    binary = float()
    octal = float()
    hexa = str()

    # Various fucntion are designed to get number in different types.
    # This fucntion gets number in integer and converts it to binary, octal and hexadecimal
    def getNum_int(self):
        self.num = float(input("Enter number in Integer: "))
        self.binary = inttobin(self.num)
        self.octal = inttooct(self.num)
        self.hexa = inttohex(self.num)

    # This Fucntion gets number in binary and converts it to integer, octal and hexadecimal

    def getNum_bin(self):
        self.binary = float(input("Enter Number in Binary: "))
        self.num = bintoint(self.binary)
        self.octal = inttooct(self.num)
        self.hexa = inttohex(self.num)

    # This function takes number in octal and convert it to integer, binary and hexadecimal

    def getNum_octal(self):
        self.octal = float(input("Enter Number in Octal: "))
        self.num = octtoint(self.octal)
        self.binary = inttobin(self.num)
        self.hexa = inttohex(self.num)

    # This function takes input in hexadecimal and convert it to integer, binary and octal

    def getNum_hex(self):
        self.hexa = input("Enter Number in HexaDecimal: ")
        self.num = hextoint(self.hexa)
        self.binary = inttobin(self.num)
        self.octal = inttooct(self.num)


    # This fucntion print all the values of object.

    def printDetails(self):
        print("Integer     :- ", self.num)
        print("Binary      :- ", self.binary)
        print("Octal       :- ", self.octal)
        print("Hexadecimal :- ",self.hexa)


# Create a object to access class.
sample = number()

# Give Choices to user.
print(Fore.CYAN,Style.BRIGHT)
print("::::NUMBER SYSTEM CONVERSIONS::::")
print(Fore.RESET,Style.NORMAL)

print("Which Data Type are you going to enter: ")
print("1 For Integer")
print("2 For Binary")
print("3 For Octal")
print("4 For HexaDecimal.")

# Ask for choices.
choice = int(input("Enter Choice:: "))

# Work on choice:
if choice == 1:
    sample.getNum_int()

elif choice == 2:
    sample.getNum_bin()

elif choice == 3:
    sample.getNum_octal()

elif choice == 4:
    sample.getNum_hex()

else:
    print("Invalid Choice.")

# Print Details
sample.printDetails()

#Created by Harsh Verma (github.com/harshverma27)
