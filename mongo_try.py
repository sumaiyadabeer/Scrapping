from pymongo import MongoClient



#from pymongo import Connection

if __name__ == "__main__":
	#conn= Connection()
	client = MongoClient()
	db = client.test_database

	people = db.people


	people.insert({'name': 'summ', 'food':'food1'})
	people.insert({'name': 'summ2', 'food':'food2', 'location': 'india'})
	people.insert({'name': 'summ3', 'food':'food3'})


	peeps = people.find() # or find_one with constrain in dictionary or regular expr

	for i in peeps:
		print(i)