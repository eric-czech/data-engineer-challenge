Data Engineering Challenge
=======================


Collaborative efforts in music are always a gamble.  While much of top 40 music consists of content resulting from partnerships between two or more artists, there are risks involved with bringing together such artists who may have opposing styles and motives.  However, these risks are often worth the reward and juxtapositions of contrasting styles have led to some very successful efforts like those from Eminem and Dido ([Stan](https://www.youtube.com/watch?v=gOMhN-hfMtY)), P!nk and Nate Ruess ([Just Give Me a Reason](https://www.youtube.com/watch?v=OpQFFLBMEPI)), or even Lady Gaga and Kermit the Frog ([Gypsy](https://www.youtube.com/watch?v=WOvxX7SHKiE)). 

These partnerships aren't always between men and women but a lot of the more interesting ones are.  In this challenge, you'll use a (fictituous) dataset to try to determine what pairings like this (i.e. between male and female artists) would be most "interesting" based on the sentiment within statements made by users online.  The sentiment of each statement will fall into one of 3 categories, positive, negative, or neutral.  Your job will then be to pair the artists up and draw conclusions about the sentiment around each pair.


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
user1     | Sam Smith | male | 1 |
user2     | Sam Smith | male | 1 |
user1     | Meghan Trainor | female | -1 |
user2     | Meghan Trainor | female | -1 |
user1     | Garth Brooks | male | 1 |
user2     | Garth Brooks | male | 1 |
user3     | Garth Brooks | male | 0 |
user4     | Garth Brooks | male | -1 |


Questions
==========

These questions all pertain to the data above and we only ask for answers to the first two, but if you're enjoying the problem then we would love to see answers to the others too.

##Question 1: Sentiment Dissonance

Using [Apache Pig](#apache-pig) (see next section for more details on it), determine the which pairs of male and female artists have the largest **difference** in cumulative sentiment.  We'll assume this difference would make the pairing more "interesting" since the public opinion about each is polarized.

An answer to this question should first determine the "net sentiment" for each artist.  For example, _Garth Brooks_ is mentioned in the example dataset above 4 times and the net sentiment for him over all mentions is 1 + 1 + 0 + -1 = 1.  This value should be calculated for each artist and then all the male and female artists should be paired together and ordered by the absolute value of the difference in that value for each pair.

A result for the example dataset would be (ordered by difference):

female.artist | male.artist | sentiment.difference
--------------|-------------|---------------------
Meghan Trainor | Sam Smith | abs(-2 - 2) = 4
Meghan Trainor | Garth Brooks | abs(-2 - 1) = 3
Miley Cyrus | Sam Smith | abs(0 - 2) = 2
Meghan Trainor | Elton John | abs(-2 - 0) = 2
Miley Cyrus | Garth Brooks | abs(0 - 1) = 1
Miley Cyrus | Elton John | abs(0 - 0) = 0

And we'd conclude that Meghan Trainor and Sam Smith make for the best pair.

*Notes*: 

1. We don't care about pairings of same sex artists (e.g. _Garth Brooks_ and _Sam Smith_)
2. The _user.name_ field is irrelevant for this question

##Question 2: Making Decisions

Assume you run your own record label and your job is to determine what proposed male/female duet is worth producing music for.  You'll encounter these opportunities once a week over the course of a year and each time you'll have to make a decision right away, and you can only choose one song to produce that year.  For example, you might run into a chance to produce a duet for Micheal Buble and Rihanna in week 1 and then another for Kenny Chesney and Iggy Azalea in week 2 but you can't want until the end of week 2 to decide -- each opportunity expires at the end of the week in which it arose.

Finally, assume that the metric calculated in Question 1 for sentiment dissonance is a perfect estimator of success.  Each time you run into the chance to produce a song for a duet, you can calculate the value from Question 1 for it and use that to make your decision.

Given this, write a program (in python, java, or bash) that will take strings on stdin in the form ```female.artist,male.artist``` (one such pair per line) and output a decision as 'yes' or 'no' for each pair.  This program can assume that only artists seen in the input dataset for Question 1 will be used and that you can do anything within the program you'd like, but you must make a decision for each pair at the time it is seen (i.e. you can't look at them all and then decide).

*Note:* No Googol-ing solutions for this please!  We'd much prefer your own approach.


##Question 3: Cohort Sentiment (Optional)

Using Pig again, determine the cumulative, net sentiment for each pair of male and female artists that are mentioned by the **same** users.

An answer to this question should first determine which artists are mentioned by the same users and then for each of those users, determine their "net sentiment" about the pairing.  For example, _user1_ in the example dataset above mentions both _Miley Cyrus_ and _Garth Brooks_ with a sentiment of 1 (i.e. positive) for each.  The "net sentiment" for that user about this artist pairing is then 1 + 1 = 2.  Keep in mind that we only care about pairs containing one male and one female artist though -- so we wouldn't care about the net value for this user in regards to a pairing of say _Elton John_ and _Garth Brooks_, who are both male artists mentioned (by _user1_).

The "cumulative" value for each male/female artist pair is then the sum of the net sentiment from each user that mentions both.  For example, the resulting value for the pairing of _Miley Cyrus_ and _Garth Brooks_ should be the sum of the net sentiment from _user1_ and _user2_, and would not include any contributions for _user3_ or _user4_ who **only** mention _Garth Brooks_.

The result for the example dataset would be:

female.artist | male.artist | cohort.sentiment
--------------|-------------|---------------------
Meghan Trainor | Sam Smith | 0
Meghan Trainor | Garth Brooks | 0
Miley Cyrus | Sam Smith | 2
Meghan Trainor | Elton John | -2
Miley Cyrus | Garth Brooks | 2
Miley Cyrus | Elton John | 0

##Question 4: Anomalies (Optional)

In all the previous questions, **net** sentiment was calculated or used to create a solution -- which is not ideal.  Considering only positive/negative/nuetral opinions like this can be useful but also involves a significant loss of information, namely how **many** opinions are being included.  A net value of 0 calculated this way could result from a single neutral opinion or 1000 opinions, half negative and half positive.

This question then will involve taking a different approach to Question 1 where instead of using net sentiment, you will use the **frequency** of each sentiment type to figure out which artist pairs are *least* like the others.  The first step in answering this question will be to compute a very similar result to Question 1 but 3 statistics instead of 1, like this:

female.artist | male.artist | num.positive  | num.negative | num.neutral
--------------|-------------|---------------------|--------------------|------------------
Meghan Trainor | Sam Smith | 2 | 2 | 0
Meghan Trainor | Garth Brooks | 2 | 3 | 1
.. and so on ...

Note that the sign or value of the sentiment no longer matters -- the result above includes only the count of the number of occurrences each sentiment type for a specific artist pair.

Given these frequencies, we ask that you determine which 10 artist pairs are *least* like the others.  For example, if we were to ignore neutral sentiment for now and just consider positive and negative sentiment, then this is how the different artist pairings relate to one another:

(each dot corresponds to a single artist pair)

<img src="https://dl.dropboxusercontent.com/u/65158725/data-challenge-scatter-plot.png"/>



Apache Pig
=============

Pig is a high-level, imperative-style programming language that is great for data munging.  As a relational algebra, it looks a lot like SQL but is much better for chaining operations together into more complicated workflows.

We installed pig, python, and java (using [Mortar](https://www.mortardata.com/products/mortar-free)) on an EC2 instance that you can use.  After we give you everything you'd need to know to login (as user ```nbs```), you'll find everything you need in the directory ```/home/nbs/data_engineer_challenge```.

We started on a Pig script for you that will read the input data from the correct place (```~/data_engineer_challenge/data/sentiment```) and count the number of times each artist is mentioned.  Here is an example of how to run that script as well as the expected output:

```
nbs@ip-10-169-43-241:~$ cd data_engineer_challenge/
nbs@ip-10-169-43-241:~/data_engineer_challenge$ mortar local:run pigscripts/sentiment.pig 

Launching Pig: 3 jobs scheduled
Full logs will be written to logs/local-pig.log

Starting job job_local_0001
Map 001: 100%       Input records:  1	Output records: 1

... [ Omitting some output for brevity ] ...

Pig run completed in 21 seconds. 3/3 jobs successful.

(artist1,1)
Success! - No error expected.
```

The ```mortar local:run``` command should be all you need to run any pigscripts you create or modify in ~/data_engineer_challenge/pigscripts.  The example script, sentiment.pig, looks like this:

```
-- Load raw data from csv files in project data directory using comma delimiter
raw = LOAD '/home/nbs/data_engineer_challenge/data/sentiment' USING PigStorage(',') 
  AS (user_name:chararray, artist_name:chararray, artist_gender:chararray, sentiment:int);

-- Group all the mention records by artist name
grouped = GROUP raw BY artist_name;

-- Determine the number of records associated with each artist
counts = FOREACH grouped GENERATE group AS artist_name, COUNT(raw) AS count;

-- Order the results by the number of records per artist
result = ORDER counts BY count DESC;

-- Print the results to stdout
DUMP result;

```

Hopefully that seems pretty intuitive.  There are many tutorials out there like [this one](http://hortonworks.com/hadoop-tutorial/how-to-process-data-with-apache-pig/), and for the sake of answering the questions you shouldn't have to learn about many Pig constructs other than the basic ones like [FOREACH](http://pig.apache.org/docs/r0.12.0/basic.html#foreach), [JOIN](http://pig.apache.org/docs/r0.12.0/basic.html#join-inner), [GROUP](http://pig.apache.org/docs/r0.12.0/basic.html#group), [ORDER](http://pig.apache.org/docs/r0.12.0/basic.html#order-by), [CROSS](http://pig.apache.org/docs/r0.12.0/basic.html#cross), and [STORE](http://pig.apache.org/docs/r0.12.0/basic.html#store)/[LOAD](http://pig.apache.org/docs/r0.12.0/basic.html#load).  There are a lot of others available though so you might find some fancy ways to use them.  The version of Pig installed is 0.12 and you can find the [full documentation here](http://pig.apache.org/docs/r0.12.0/).




