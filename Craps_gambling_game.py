from random import randint

money=1000
while money>0:
    needs_go_on=False
    while True:
        debt=int(input("Please bet: "))
        if 0<debt<=money:
            break
    first=randint(1,6)+randint(1,6)
    print("The player shakes out %d points"%(first))
    if first==7 or first==11:
        print("Player wins")
        money+=debt
        print(money)
    elif first==2 or first==3 or first==12:
        print("Banker wins")
        money-=debt
        print(money)
    else:
        needs_go_on=True
    while needs_go_on:
        needs_go_on=False
        current=randint(1,6)+randint(1,6)
        if current==7:
            print("Banker wins")
            money-=debt
            print(money)
        elif current==first:
            print("Player wins")
            money+=debt
            print(money)
        else:
            needs_go_on=True
    
print("You're bankrupt, the game is over!")
    
    
