#Functions

def format_destination_info(city,country,population=""):
	"""This function format's these two values in correct order & merges them into a single value."""

	destination = ""
	if population:
		destination = city+", "+country+" - population : "+population
	else:
		destination = city+", "+country

	return destination.title()	
