Data Engineering Challenge
=======================


Collaborative efforts in music are always a gamble.  While much of top 40 music consists of content resulting from partnerships between two or more artists, there are inevitable risks inherent to bringing together such artists who often have opposing styles and motives.  However, these risks are often worth the reward and juxtapositions of contrasting styles have led to some very successful efforts like those from Eminem and Dido ([Stan](https://www.youtube.com/watch?v=gOMhN-hfMtY)), P!nk and Nate Ruess ((Just Give Me a Reason)[https://www.youtube.com/watch?v=OpQFFLBMEPI]), or even Lady Gaga and Kermit the Frog ([Gypsy](https://www.youtube.com/watch?v=WOvxX7SHKiE)). 

These partnerships aren't always between men and women but a lot of the more interesting ones are.  In this challenge, you'll use a (fictituous) dataset to try to determine what pairings like this (i.e. between male and female artists) would be most "interesting" based on the sentiment within statements made by users online.  The sentiment of each statement will fall into one of 3 categories, postivie, negative, or neutral.  Your job will be to find which pairs are often mentioned online by the _same_ people and then use the sentiment associated with those mentions to figure out which pairings would be ideal.


Dataset
===========

The input dataset will consist of the following things:

- _user.name_ - The screenname of the user that mentioned the artist
- _artist.name_ - The name of the artist mentioned
- _artist.gender_ - The gender of the artist (either 'male' or 'female')
- _sentiment_ - The attitude within the statement made (either 1, -1, or 0 for positive, negative, and neutral respectively)

For example:

user.name | artist.name | artist.gender | sentiment |
----------|-------------|---------------|-----------|
user1     | Miley Cyrus | female | 1 |
user2     | Miley Cyrus | female | -1 |
user1     | Elton John | male | 1 |
user2     | Elton John | male | -1 |
user1     | Nicki Minaj | female | 0 |
user2     | Nicki Minaj | female | 0 |
user1     | Sam Smith | male | 1 |
user2     | Sam Smith | male | 0 |
user1     | Meghan Trainor | female | -1 |
user2     | Meghan Trainor | female | -1 |
user1     | Garth Brooks | male | 1 |
user2     | Garth Brooks | male | 1 |


Questions
==========

These questions all pertain to the data above and we only ask for answers to the first two, but if you're enjoying the problem then we would love to see answers to the others as well (they appear roughly in order of difficulty).

_Question 1_ - Determine the cumulative, net sentiment for each pair of male and female artists that are mentioned by the same user.

An answer to this question should first determine which artists are mentioned by the same users and then for each of those users, determine their "net sentiment" about the pairing.  For example, _user1_ in the example dataset in the previous section mentions both _Miley Cyrus_ and _Elton John_ with a sentiment of 1 (i.e. positive) for each.  The "net sentiment" for that user about this artist pairing is then 1 + 1 = 2.  Keep in mind that we only care about pairs containing one male and female artist though -- so we wouldn't care about the net value for this user in regards to a pairing of say _Elton John_ and _Garth Brooks_, who are both male artists mentioned (by _user1_).

The "cumulative" value for each male/female artist pair is then the sum of the net sentiment from each user.




