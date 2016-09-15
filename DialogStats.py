from __future__ import division
from collections import Counter
import re
import csv
from nltk.util import bigrams,trigrams


f = open('dialogue.txt', 'r')

dialogueTurns = {}
totalWords = {}
distribution = {}
avgWordsPerTurn = {}
avgWordLength = {}
count = 0
count_a = 0
count_b = 0
lineArray = []
lineArray_a = [] 
lineArray_b = []

for speaker in ['A', 'B']:
	dialogueTurns[speaker] = 0
	totalWords[speaker] = 0
	avgWordsPerTurn[speaker] = 0
	avgWordLength[speaker] = 0
	distribution[speaker] = []

for line in f:

	if re.match("^\d", line): # Parse only dialogue lines which start with some number in the beginning

		# sub everything other than whitespace, alphabets, numbers. Remove whitespace at end.
		line = re.sub("[^\w\s]", '', line).rstrip()
		wordArray = re.split("\s+", line)
		
		# Array index 0 and 1 contain irrelevant data, index 2 contains the speaker identifier, rest are words
		speaker = wordArray[2]
		wordArray = wordArray[3:]
		
		#Adding lists for corpus data for individual and collective analysis
		for word in wordArray:
			if speaker == 'A':
				lineArray_a.append(word)
			elif speaker == 'B':
				lineArray_b.append(word)
			lineArray.append(word)

		dialogueTurns[speaker] += 1
		totalWords[speaker] += len(wordArray)
		distribution[speaker].append(len(wordArray))
		avgWordsPerTurn[speaker] = totalWords[speaker] / dialogueTurns[speaker]

		if speaker == 'A' and re.search("show", line):
			count_a += 1
		elif speaker == 'B' and re.search("show", line):
			count_b += 1

		for word in wordArray:

			avgWordLength[speaker] += (len(word) - avgWordLength[speaker]) / totalWords[speaker]




writer = csv.writer(open("result.csv", 'w'))
headers = ["Interlocutor", "dialogueTurns", "totalWords", "avgWordsPerTurn", "avgWordLength"]
col_width = max(len(word) for word in headers) + 2
writer.writerow(headers)
print ''.join(header.ljust(col_width) for header in headers)

for speaker in ['A', 'B']:
	row = [speaker, str(dialogueTurns[speaker]), str(totalWords[speaker]), str(avgWordsPerTurn[speaker]), str(avgWordLength[speaker])]
	writer.writerow(row)
	print ''.join(val.ljust(col_width) for val in row)

print "Total number of utterances by A containing the word show: ", count_a
print "Total number of utterances by B containing the word show: ", count_b

print "Total number of utterances containing the word show: ", count_a + count_b

a_not_word = dialogueTurns["A"] - count_a
b_not_word = dialogueTurns["B"] - count_b

print "Total number of utterances by A not containing the word show: " , a_not_word
print "Total number of utterances by B not containing the word show: " , b_not_word
print "Total number of utterances not containing the word show: ", a_not_word + b_not_word

print "P(u is from Speaker 1): ", dialogueTurns["A"] / (dialogueTurns["A"] + dialogueTurns["B"])
print "P(u is from Speaker 2): ", dialogueTurns["B"] / (dialogueTurns["A"] + dialogueTurns["B"])
print "P(u contains \"show\" | u is from Speaker 1): ", count_a /  (dialogueTurns["A"])
print "P(u being from Speaker 1 | u contains \"show\"): ", count_a /  (count_a + count_b)
print "P(u beding from Speaker 1 | u does not contain \"show\"): ", a_not_word /  (a_not_word + b_not_word)
print "P(u being from Speaker 2 | u contains \"show\"): ", count_b /  (count_a + count_b)

#print "Word Counts: ",word_counts

#print lineArray
#count = 
most_common_word = Counter(lineArray).most_common(1)
most_common_word_A = Counter(lineArray_a).most_common(1)
most_common_word_B = Counter(lineArray_b).most_common(1)
print "The most common token in the corpus is: \"",most_common_word[0][0],"\" which occured", most_common_word[0][1], "times"
print "The most common token in the corpus by A is: \"",most_common_word_A[0][0],"\" which occured", most_common_word_A[0][1], "times"
print "The most common token in the corpus by B is: \"",most_common_word_B[0][0],"\" which occured", most_common_word_B[0][1], "times"

print "The most common bigram in the corpus is: ", Counter(list(bigrams(lineArray))).most_common(1)[0][0]
print "The most common trigram in the corpus is: ", Counter(list(trigrams(lineArray))).most_common(1)[0][0]

file_A = open("A_distribution.txt", "w+")
file_B = open("B_distribution.txt", "w+")

file_A.write(" ".join(str(x) for x in distribution["A"]))
file_B.write(" ".join(str(y) for y in distribution["B"]))
# file_A.write(str(distribution["A"]))
# file_B.write(str(distribution["B"]))

# print "\nSuccess! Output is in result.csv"	

f.close()
file_A.close()
file_B.close()
