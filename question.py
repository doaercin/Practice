
class Map:
	def __init__(self) -> None:
		self.cities = []
	
	def add_city(self, city):
		self.cities.append(city)
		return City(city)
	
	def print(self):
		for city in self.cities:
			print (city, "=>", end=" ;")
			for school in city.schools:
				print(school.list(), end=" ")


class City:
	def __init__(self,city) -> None:
		self.city = city
		self.schools = []

	def add_school(self,school):
		self.schools.append(school)
		return School()


class School:
	def __init__(self) -> None:
		pass


class University(School):
	def __init__(self,uni) -> None:
		self.uni = uni
	

	def list(self):
		return (self.uni, "University")


class HighSchool(School):
	def __init__(self,hs,language):
		self.hs = hs
		self.language = language

	def list(self):
		return (self.hs, "HighSchool", self.language)


# Add your code before this line. Do not change the code below this line.

def Run():
	m = Map()
	C1 = m.add_city(City("Istanbul"));
	C2 = m.add_city(City("Konya"));

	C1.add_school(University("BU"));
	C2.add_school(University("Selcuk"));
	C1.add_school(University("ITU"));
	C1.add_school(HighSchool("DSI", "German"));
	C1.add_school(HighSchool("GS", "French"));
	C2.add_school(HighSchool("KAL", "English"));

	return m.print()

