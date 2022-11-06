#This File contain fucntion to convert octal number to integer

def octtoint(n: float):

    #Used basic method of multipltying numbers with decreasing powers of 8
    intans = 0
    intpart = int(str(n).partition('.')[0])
    intpart = str(intpart)[::-1]

    #We can also multiply by increaing power of 8 by using numbers in reverse order.
    for i in range(len(intpart)):
        intans += int(intpart[i]) * pow(8,i)

    #For floating part we used the method which includes multplying numbers with increasing neagative powers of 8.
    floatans = 0 
    floatpart = str(n).partition('.')[2]

    #The powers are actually decreasing, but -i is increasing.
    for i in range(0,len(floatpart)):
        floatans += pow(8,-(i+1)) * int(floatpart[i])

    #Finally we will return the sum of both the answers
    return intans + floatans
#Created by Harsh Verma (github.com/harshverma27)

