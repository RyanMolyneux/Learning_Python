#Chapter 10 ex 5 date :	07/07/17.

#Variable
file = "programming_reasons.txt"

#Body

while(True):
	text = input("\n\nPlease enter why you love programming\n\n Reason : ")
	
	with open(file,"a") as reasons:
		if(text.lower() != "finished"):
			reasons.write("\n--------------------\nVIEW\n--------------------\n"+text)
			
		else:
			break
