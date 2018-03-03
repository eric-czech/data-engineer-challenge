from organize import organize

def average():
	"""
	This function will find the average pairing sentiment from all possible paring combinations.
	This will be used to determine whether or not an artist pairing will be chosen or not.
	"""
	sum = 0

	(male,female)= organize("sentiment.csv")

	for a,b in male.items():
		for y,z in female.items():
			sum = sum+b+z
			
	mean = sum/(len(male)*len(female))

	return mean

