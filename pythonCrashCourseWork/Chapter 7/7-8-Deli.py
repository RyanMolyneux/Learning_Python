#Chapter 7 ex 8 date : 18/06/17.

#Variables
sandwhich_orders = ["tuna sandwhich","bacon&egg","chicken&stuffing"]
finished_sandwhichs = []
#Main Body

while sandwhich_orders:
	sandwhich = sandwhich_orders.pop()
	print("\n\nYour ",sandwhich," is ready!!!")
	finished_sandwhichs.append(sandwhich)

print("\n-----------------------------------------\n\tFinished sandwhichs history\n-----------------------------------------\n")
for sandwhich in finished_sandwhichs:
	print("\n",sandwhich)