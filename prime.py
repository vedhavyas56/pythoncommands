number=int(input(" enter any number : "))
flag=1
for i in range(2, int(number/2)):
    if number%i==0:
        flag=0
        break
if flag==1 and number>=2:
    print(" given number is prime  ",number)
else:
   print ("given number is not a prime number ",number)