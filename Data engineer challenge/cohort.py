from organize import super_organize
def cohort():
	"""
Cohort will output a dictionary called duo that has all the possible male and female artist pairings
that are mentioned by users who mention both male and female artists. Dictionary's form will be
 {"male_artist and female_artist": sentiment, ...}

cohort uses the dictionary passed through by super_organize. It goes through each male and female pairing
submitted by each user, and either adds the pair to the dictionary duo with their respective sentiment
if the pair isn't included, or adds to the total sentiment if the pair already exists in duo.

	"""
	users = super_organize("sentiment.csv")
	duo={}
	for user,data in users.items():
		for males,pointsm in data[0].items():
			for females,pointsf in data[1].items():
				if males+ " and " + females not in duo:
					duo[males+ " and " +females] = pointsm + pointsf
				else:
					duo[males+ " and " +females] = duo[males+ " and " +females] + pointsm + pointsf
	return(duo)