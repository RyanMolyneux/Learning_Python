#Classes
class	School:
	"School class will contain information about the school that students Are attending.";
	#Class Variables
	__stuCount = 0;
	name = "St Aidans";
	yearOpen = 1993;
	numClasses = 20;

	#Methods
	def	incrementStudentCount():
		"Used to increment the number of students attending the school";
		return;

	



class Student(School):
	"Student class which will contains both class variables & instance."
		

	#Constructors
		#Default
	def	__init__(self,firstName,lastName,age,parents,classes):
		self.firstName = firstName;
		self.lastName = lastName;
		self.age = age;
		self.parents = parents;
		self.classes = classes;
		self.incrementStudentCount;

								