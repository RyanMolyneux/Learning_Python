#Chapter 8 ex 7 date : 21/06/17.

#Variables
albums = []

#Functions
def make_album(artistName,albumTitle,num_tracks = ""):
	"Creates a dictionary made up of music artist albums."

	album = {"artist" : artistName,"album title": albumTitle}

	if num_tracks:
		album["number of tracks"] = num_tracks
		
	return album
#Body

print("\n--------------------------------------\n\tStore Your Favourites Today\n--------------------------------------\n\nExample ",make_album("Jimmo","Jambo","3"))

for album in range(0,3):
	albums.append(make_album(input("\n\nPlease enter artist name : "),input("Please enter album title :")))

while albums:
	print("\nAlbums\n---------------------------\n",albums.pop())