# This File contains function to convert integer to Hexadecimal

# This Converts a list hexadecimal number greator than 9 to thier respective alphabet
def alphaModify(s: list):
    ans = []

    # Used basic method of iterating thorough entire list and changing any number greator than 9.
    for i in s:
        if int(i) < 10:
            ans += i
        else:
            ans += chr(55+int(i))  #the chr() function actually returns alphabet based on acii provided.
    
    #returning the list prepared.
    return ans

def inttohex(n: float):

    # Multiplying Number to get rid of decimal
    n *= pow(16, 8)
    n = round(n)

    # Doing basic method of storing remainders then reversing them.
    temp = []
    while (n > 0):
        temp.append(str(n % 16))
        n //= 16
    ans = ""
    temp = temp[::-1]
    temp = alphaModify(temp)

    # Now we have to put '.' 8 digits before last
    for i in range(len(temp)):
        if len(temp) - i > 8:
            ans += temp[i]
        elif len(temp) - i == 8:
            ans += '.'
        elif len(temp) - i < 8:
            ans += temp[i-1]

    # Our answer is ready
    return ans
    