age = int(input("enter your age : "))
print("person age", age)

if (age <12):
    print("Child")
else:
    if(age <18):
        print("Teen")
    else:
        if (age < 27):
            print("Adult")
        else:
            if (age < 45):
                print("midleage")
            else:
                if (age < 64):
                    print("Senior")
        