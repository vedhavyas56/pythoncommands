telugu=90
english=85
sanskrit=73
maths=33
social=90
if(telugu>english and telugu>sanskrit and telugu>maths and telugu>social):
	print("The  highest marks of all subjects",telugu)
else:
	if(english>telugu and english>sanskrit and english>maths and english>social):
		print("The  highest marks of all subjects",english)
	else:
		if(sanskrit>telugu and sanskrit>english and sanskrit>maths and sanskrit>social):
			print("The  highest marks of all subjects",sanskrit)
		else:
			if(maths>telugu and maths>sanskrit and maths>english and maths>social):
				print("The  highest marks of all subjects",maths)
			else:
				print("The The  highest marks of all subjects",social)
total=telugu+english+sanskrit+maths+social
print("the total of all subjects",total)
average=total/5
print("the average percentage of all subjects",average)
if(telugu<english and telugu<sanskrit and telugu<maths and telugu<social):
	print("The lowest marks among all subjects",telugu)
else:
	if(english<telugu and english<sanskrit and english<maths and english<social):
		print("The lowest marks among all subjects",english)
	else:
		if(sanskrit<telugu and sanskrit<english and sanskrit<maths and sanskrit<social):
			print("The lowest marks among all subjects",sanskrit)
		else:
			if(maths<telugu and maths<sanskrit and maths<english and maths<social):
				print("The lowest marks among all subjects",maths)
			else:
				print("The lowest marks among all subjects",social)
if(telugu<35):
    print("failed subjects telugu",telugu)
else:
    if(english<35):
        print("failed subjects english",english)
    else:
          if(sanskrit<35):
              print("failed subjects sanskrit",sanskrit)
          else:
              if(maths<35):
                  print("failed subjects maths",maths)
              else:
                  print("failed subjects social",social)  
        