number=[1,2,3,4,5,6]
print(number[0])
print(number[4])

print(number[-1])
print(number[-4])

#replacing the values
number[4]=10
print(number)

#write a pythpn progarmm by using python list and print multiplication values from the selected item in the list 
print("multiply the selected values ")
number[3]=number[2]*5
print(number)
#%
number[1]=number[3]%1
print(number)

print("appending the new value to existed list")
number.append(20)
print(number)

print("\n inserting a new value in existed list of value" )
number.insert(3,400)
print(number)


print("\n deletingthe element for existed list of values")
del number[2]
print(number)


print("\n poping the particular element from givenlist by pop method ")
last=number.pop()
print(last)
print(number)

third=number.pop()
print(third)
print(number)


print("\n removing the element from given list :")
number.remove(400)
print(number)



