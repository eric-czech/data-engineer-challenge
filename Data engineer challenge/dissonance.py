from organize import organize
"""
Goes through all male and female artists (seperatly), and finds the best and worst male and female artist.
Then goes through all combinations of best/worst male/female artists and finds the one with the largerst 
sentiment difference and prints the artist pair with the largest sentiment. 
"""

bestmale= "someone"
worstmale= "someone"
bestfemale= "someone"
worstfemale= "someone"
bestmalenum= 0
worstmalenum= 0
bestfemalenum= 0
worstfemalenum= 0

(male,female)= organize("sentiment.csv")

for x, y in male.items():
	if y > bestmalenum:
		bestmalenum=y
		bestmale=x
	if y < worstmalenum:
		worstmalenum=y
		worstmale=x


for x, y in female.items():
	if y > bestfemalenum:
		bestfemalenum=y
		bestfemale=x
	if y < worstfemalenum:
		worstfemalenum=y
		worstfemale=x

bestmalenum=abs(bestmalenum)
bestfemalenum=abs(bestfemalenum)
worstmalenum=abs(worstfemalenum)
worstfemalenum=abs(worstfemalenum)


a = bestmalenum+worstfemalenum
b = bestmalenum+bestfemalenum
c = worstmalenum+worstfemalenum
d = worstmalenum+bestfemalenum

stats = [a,b,c,d]

highest = max(stats)

if highest == a :
	print(bestmale + " and " + worstfemale)
if highest == b:
	print(bestmale + " and " + bestfemale)
if highest == c:
	print(worstmale + " and " + worstfemale)
if highest == d:
	print(worstmale + " and " + bestfemale)
