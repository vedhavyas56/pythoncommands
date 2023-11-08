rates=[50,60,20]
print(rates)

iterator=map(lambda rates: rates*5 , rates)
print(list(iterator))
