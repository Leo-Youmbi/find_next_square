from math import sqrt
def find_next_square(sq):
    ans = sqrt(sq)
    if ans.is_integer() == True: 
        return (ans+1) **2
    return -1

print(find_next_square(36))
#or
"""
def find_next_square(sq):
    return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1
"""
