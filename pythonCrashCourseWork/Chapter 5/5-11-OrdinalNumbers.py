#Chapter 5 ex 11 date : 11/06/17.

#Variables
ordinals = list(range(1,10))


#Main Body
for ordinal in ordinals:
	if(ordinal == 1):
		print(ordinal,"st")		
	elif(ordinal == 2):
		print(ordinal,"nd")
	elif(ordinal == 3):
		print(ordinal,"rd")
	else:
		print(ordinal,"th")