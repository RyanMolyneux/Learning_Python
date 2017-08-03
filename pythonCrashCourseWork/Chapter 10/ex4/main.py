#Chapter 10 ex 4 date : 07/07/17.

#Variables
file = "visitation_list.txt"

#Functions
def record_visits(file):
	while(True):
		text = input("Please Enter name to record visitation \nInput : ")
		if text.lower() != "finished":
			with open(file,"a") as visitations:
				visitations.write("\n-----------------\n"+text)
		else:
			print("\n\nThank you for using visitation creators .com.")
			break
#Main

record_visits(file)
			