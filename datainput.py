telugu= int(input('entertelugu subject marks:'))
hindi= int (input('enter  hindi subject marks:'))
maths= int (input('enter  maths subject marks:'))
biology= int (input('enter  biology subject marks:'))
social= int (input('enter  social subject marks:'))

print("\n given subject marks are",telugu)
print("\n given subject marks are",hindi)
print("\n given subject marks are",maths)
print("\n given subject marks are",biology)
print("\n given subject marks are",social)

total=telugu+hindi+biology+maths+social
print("th sum of total marks are",total)

if(telugu>hindi and telugu>maths and telugu>biology and telugu>social):
    print("The  highest marks of all subjects",telugu)
else:
    if(hindi>telugu and hindi>maths and hindi>biology and hindi>social):
        print("The  highest marks of all subjects",hindi)
    else:
        if(maths>telugu and maths>hindi and maths>biology and maths>social):
            print("The  highest marks of all subjects",maths)
        else:
            if(biology>telugu and biology>sanskrit and biology>maths and biology>social):
                print("The  highest marks of all subjects",biology)
            else:
                print("The The  highest marks of all subjects",social)
average=total/6
print("the avergae percentage of all subjects",average)
