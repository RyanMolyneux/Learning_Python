#Chapter 3 ex 8 date 10/06/17.

#Variables
visit_list = ["nyc","tokoyo","silicon valley","spain","greece"]

print("\n\nPlace I would love to visit\n--------------------------\n",visit_list[0],"\n",visit_list[1],"\n",visit_list[2],"\n",visit_list[3],"\n",visit_list[4])

print("\n\nThese Destinations in alphabetical order\n--------------------------\n",sorted(visit_list))

print("\n\nPace I would like to visit in none alpabetical order\n--------------------------\n",visit_list[0],"\n",visit_list[1],"\n",visit_list[2],"\n",visit_list[3],"\n",visit_list[4])

print("\n\nDestinations in reverse alpabetical order\n--------------------------\n\n",sorted(visit_list,reverse=True))

print("\n\nOrigional order of list\n--------------------------\n",visit_list)

visit_list.reverse()

print("\n\nReversed order of list\n--------------------------\n",visit_list)

visit_list.reverse()

print("\n\nChanged back to origional order of list\n--------------------------\n",visit_list)

visit_list.sort()

print("\n\nList has permanently been altered to from its origional order & is now in alphabetic\n--------------------------\n",visit_list)

visit_list.sort(reverse=True)

print("\n\nList changed from alphabetic to reverse alphabetic order\n--------------------------\n",visit_list)