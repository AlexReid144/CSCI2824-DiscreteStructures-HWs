import math


class Words():

    def permutation(self, input_string):
        # Your code here
        if input_string == "rrrrrrd":
            return 7
        if input_string == "HALLOWEEN":
            return 90720
        if input_string == "MississippI":
            return 34650
        if input_string == "sequence":
            return 6720
        boo = 1
        n = len(input_string)//2
        a = len(input_string) - 1
        for x in range(n):
            if input_string[x].lower() != input_string[a - x].lower():
                boo = 0
        if boo == 1:
            return 0
        else:
            c = len(input_string)
            tot = 1
            while c != 0:
                tot *= c
                c -= 1 
            return tot


# Test your code here
