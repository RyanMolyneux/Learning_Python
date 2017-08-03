#Chapter 3 ex  6 date : 10/06/17.

#Variables
guest_list = ["Sam","Johnny","Timmy"]

print("\n\nGuest List\n------------------------------\n",guest_list[0],"\n",guest_list[1],"\n",guest_list[2],"\n\nI would like to invite you all to some delicious dinner at mine\n\nalso as I have obtained a bigger dining table I may invite more so this list is open to change.\n\n")

guest_list.insert(0,"Jane")
guest_list.insert(2,"Zoey")
guest_list.append("Zara")

print("\n\nNew Guest List\n------------------------------\n",guest_list[0],"\n",guest_list[1],"\n",guest_list[2],"\n",guest_list[3],"\n",guest_list[4],"\n",guest_list[5],"\n\nYou have all been invited to dine with me at home.")