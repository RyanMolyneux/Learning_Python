#Chapter 3 ex 7 date: 10/06/17

#Variables
guest_list = ["Joe","zoEl","Kara"]

guest_list.insert(0,"Kale")
guest_list.insert(2,"Kane")
guest_list.append("Able")

print("\nNew Guest List\n---------------------------\n\n",guest_list[0],"\n",guest_list[1],"\n",guest_list[2],"\n",guest_list[3],"\n",guest_list[4],"\n",guest_list[5],"\n\nI am sorr to announce that the larger dining table will not arrive in time so i am pressed to onl invite 2 of you.\n\nThose UnInvited are\n-------------------------------\n\n",guest_list.pop(),"\n",guest_list.pop(),"\n",guest_list.pop(1),"\n",guest_list.pop(0),"\n\nGuest List Now\n------------------------------\n",guest_list[0],"\n",guest_list[1],"\n\nYou two are still invited.")
#Deleting items from guest list
del guest_list[0]
del guest_list[0]

print("\n\nCurrent Guests after clearing\n\n",guest_list)