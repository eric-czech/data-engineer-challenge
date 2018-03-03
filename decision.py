from average import average
from organize import organize


def decision():
	"""
	This function will determine whether or not the artist pairing submitted by the user will be accepted or not.
	Pairing will be accepted if the net sentiment of both artistsis greater than or equal to the average sentiment 
	of all possible male,female pairings.

	I know an average is a basic approach to this problem, but this is more to me of a data acquitition practice set
	than a statistical practice set.

	User will be asked to name a female and male pairing in one line upon start such as female,male. 
	Input is not case or space sensitive, however each artist must exist in data set or else an error message will appear.

	Program will restart after each input. Only if input is "exit" will the program leave the loop.
	"""
	print("Type exit to leave")
	name = input('Name a female and male artist like female, male: ')
	if name == "exit":
		return
	artists = name.split(',')

	artists[0]= artists[0].title()
	artists[0]= artists[0].strip()
	artists[1]= artists[1].title()
	artists[1]= artists[1].strip()

	(male,female)= organize("sentiment.csv")

	
	if artists[0] not in female:
		print(artists[0] + " is not in list, try again")
	if artists[1] not in male:
		print(artists[1] + " is not in list, try again")

	if artists[0] in female and artists[1] in male:
		sum = female[artists[0]] + male[artists[1]]
		if sum >= average():
			print("yes")
		else:
			print("no")
		decision()
decision()
