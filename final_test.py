from llist import *
from math import gcd

def gen321():
    lst = LList()
    lst.append(3)
    lst.append(2)
    lst.append(1)
    return lst

lst = gen321()
lst.append(2)
lst.dedup()
print(lst)

lst = gen321()
lst.append(1)
lst.dedup()
print(lst)

lst = gen321()
lst.append(3)
lst.dedup()
print(lst)

lst = gen321()
lst.prepend(3)
lst.dedup()
print(lst)

lst = LList()
def genlist(n):
    f = lambda x: (x*x+1) % n
    x = y = 2
    for _ in range(n):
        x = f(x)
        y = f(f(y))
        if gcd(abs(x-y), n) != 1:
            lst.append(x)
    return lst

lst = genlist(47077)
lst.dedup()
print(lst)
