#Chapter 10 exercise 3 date : 07/07/17.

#Variables
guest_list = []

#Functions
def create_guest_list(file_name="guest_list.txt"):
	
	while(True):
		text = input("\nPlease enter the name of the guest your inviting\nInput : ")
		
		if text != "finished":
			guest_list.append(text)
			print("Guest Successfully added.")
		else:
			print("Thank you for using guests.com.")
			break

	with open(file_name,"w") as guest_file :
		guests = "Guest List"
		for item in guest_list:
			guests+= "\n--------------------\n"+item
		guest_file.write(guests)

def view_guest_list(file ="guest_list.txt"):
	with open(file) as guest_file:
		print(guest_file.read())


#Main
print("\n--------------------------------\nGuests.CoM")
file = input("\n\nPlease type filename& extemsion of the file you wish to access \nInput : ")			
create_guest_list(file)