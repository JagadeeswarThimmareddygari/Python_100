def check(num):
    temp=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:
        print("It's the palindrom number")
    else:
        print("It's not a palindrom number")


n=int(input())
check(n)
