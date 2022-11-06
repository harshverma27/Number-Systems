# This File contains function to convert integer to binary

def inttooct(n: float):

    # Multiplying Number to get rid of decimal
    n *= pow(8, 8)
    n = round(n)

    # Doing basic method of storing remainders then reversing them.
    temp = ""
    while (n > 0):
        temp += str(n % 8)
        n //= 8
    ans = ""
    temp = temp[::-1]

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
#Created by Harsh Verma (github.com/harshverma27)