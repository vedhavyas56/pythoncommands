start=int(input("\n enter starting table number :"))
for i in range(1,11):
    print("\n\n The multipliction table of %d\n "%(i))
    for j in range(1,11):
        print("%-5d x %5d = %5d" % (i,j,i*j))