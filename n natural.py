num=int(input(" \n enter any number : "))
if num<0: 
    print(" please enter a postive number")
else:
    sum=0 
    while (num>0):
        sum+=num 
        num -=1
        print ("the result value are",sum)
