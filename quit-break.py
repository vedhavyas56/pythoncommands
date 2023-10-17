print('--help: type quit to exit from the programme')
while True:
    name=input('enter any name :')
    if name.lower()=='quit':
        break 
    
print ('\n odd number :\n') ;
for number in range (100):
    if number%2==0:
        continue
    print (number)
        
        
print ("\n -- even number :\n ")
for  number in range (100):
    if number%2:
        continue    
    print (number)