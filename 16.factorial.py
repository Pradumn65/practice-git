num=input("enter the number: ");
fact=1;
for i in range(int(num)):
    fact=fact*(i+1);

print("factorial of "+str(num)+" is:"+str(fact));