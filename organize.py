def organize(file):
	"""
	organize will create two dictionaries, male and female, that have the artists's names as their key, and their
	net sentiment as their value.
	"""
	male = {}
	female = {}
	with open(file) as f:
 		for line in f:
	 		a= line.split(",")
	 		if a[2] == "male":
	 			if a[1] in male:
	 				male[a[1]] = int(male[a[1]]) + int(a[3])
	 			else:
	 				male[a[1]] = int(a[3])
	 		else:
	 			if a[1] in female:
	 				female[a[1]] = int(female[a[1]]) + int(a[3])
	 			else:
	 				female[a[1]] = int(a[3])
	return(male,female)


def super_organize(file):
	"""
	super_organize will output a dictionary called users that has each user as the key, and all the artists & sentiments
	as the value.

	Each value in the dictionary consists of a list with two dictionaries (one dictionary for male artists, the other for 
	female artist). This way I can loop through each user in another function to create a new dictionary with artist 
	male and female pairings. 
	"""
	users = {}
	with open(file) as f:
 		for line in f:
	 		a= line.split(",")
	 		user=a[0].strip()
	 		artist=a[1].strip()
	 		gender=a[2].strip()
	 		grade=int(a[3])
	 		if user not in users:
	 			data = [{},{}]
	 			if gender == "male":
	 				data[0][artist]=grade
	 				users[user]=data
	 			else:
	 				data[1][artist]=grade
	 				users[user]=data
	 		else:
	 			if gender == "male":
	 				users[user][0][artist]=grade
	 			else:
	 				users[user][1][artist]=grade
	return(users)
