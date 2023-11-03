number=(5,)
print(type(number))

#assiging the tuple variable
colour=('red','green','white')
print(colour)

colour=('cyan','green','black')
print(colour)


#sort
print("\n sorting the value: ")
guests=['ravindra','rajesh','sai','ganesh']
guests.sort()
print(guests)


#reverse
guests=['1','2','3','4']
guests.sort(reverse=True )
print(guests)


companies=[('tcs','2019','13.98')
           ,('apple','400','26.03')
           ,('hand book','2010','80.48')]
def sort_key(company):
    return company[2]
companies.sort(key=sort_key,reverse=True)
print(companies)


companies=[('tcs','2019','13.98')
           ,('apple','400','26.03')
           ,('hand book','2010','80.48')]
companies.sort(key=lambda company :company[2])
print(companies)
         