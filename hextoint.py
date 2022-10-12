#This File contain fucntion to convert octal number to integer

#This fucntion convert any alphabet containign list to thier respective numbers
def alphaModify(s: str):
    lst = []
    
    #Iterate thorugh list, and change if any alphabet found
    for i in s:
        if 64<ord(i)<71: #Here, ord() function actually returns ascii of argument
            lst.append(ord(i)-55)
        else:
            lst.append(i)
    
    #Return the prepared list
    return lst
def hextoint(n: str):

    #Used basic method of multipltying numbers with decreasing powers of 16
    intans = 0
    intpart = str(n).partition('.')[0]
    intpart = str(intpart)[::-1]
    intpart = alphaModify(intpart)


    #We can also multiply by increaing power of 16 by using numbers in reverse order.
    for i in range(len(intpart)):
        intans += int(intpart[i]) * pow(16,i)


    #For floating part we used the method which includes multplying numbers with increasing neagative powers of 16.
    floatans = 0 
    floatpart = str(n).partition('.')[2]
    floatpart = alphaModify(floatpart)


    #The powers are actually decreasing, but -i is increasing.
    for i in range(0,len(floatpart)):
        floatans += pow(16,-(i+1)) * int(floatpart[i])
        

    #Finally we will return the sum of both the answers
    return intans + floatans

