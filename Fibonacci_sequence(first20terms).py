nterm=20
count=0
n1,n2=0,1
while count<nterm:
    print(n2)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
