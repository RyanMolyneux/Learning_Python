#Chapter 7 ex 9 date : 18/06/17.

#Variables
sandwhich_orders = ["tuna","chicken&stuffing","pastrami","egg&bacon","pastrami"]
finished_sandwhichs = []


#Main Body

print("\n\nSeems as though we have run out of pastrami.")

while "pastrami" in sandwhich_orders:
	sandwhich_orders.remove("pastrami")

while sandwhich_orders:
	sandwhich = sandwhich_orders.pop()
	print("\n\nYour ",sandwhich," is ready!!!")
	if(sandwhich != "pastrami"):
		finished_sandwhichs.append(sandwhich)

print("\n-----------------------------------------\n\tFinished sandwhichs history\n-----------------------------------------\n")
for sandwhich in finished_sandwhichs:
	print("\n",sandwhich)