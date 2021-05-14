from random import randint

def roll_dice(n=2):
    total=0
    for i in range(n):
        total+=randint(1,6)
    return total

def add(a=0,b=0,c=0):
    print(a,b,c,sep="+")
    return a+b+c

print(roll_dice())
print(roll_dice(3))
print(roll_dice(5))

(add())


print(add(2,3))
print('---->',add(2,7,9))
print('---->',add(a=8,b=9,c=10))
