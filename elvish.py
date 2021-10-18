#!/usr/bin/env python3

import sys
import fileinput
import random
import json

random.seed(1)

# you may need to add more
puncs =  '.,1?!:;-*"_()[]{}<>/1234567890—“”’‘–$«»\'=#@%&+'
spaces = ' ' * len(puncs)

wordcount = {}
for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	# count all words because unique words may be errors of some kind
	for word in line.split():
		word += '*'
		if word not in wordcount: wordcount[word] = 0
		wordcount[word] += 1
 
# letter frequencies - looking for punctuation and such
"""
lettercount = {}
for word in wordcount:
	for letter in word:
		if letter not in lettercount: lettercount[letter] = 0
		lettercount[letter] += wordcount[word]
		
for let in lettercount:
	print(let, lettercount[let])
"""


count1 = {} # count of first letter
count2 = {} # count of second letter, given the first letter
count3 = {} # counts of third, given first and second
for word in wordcount:
	if len(word) < 4: continue
	
	# first letter counting
	c1 = word[0] # first letter
	if c1 not in count1: count1[c1] = 0
	count1[c1] += 1
	#count1[c1] += wordcount[word]
	
	# second letter counting, given the first letter
	c2 = word[1] # second letter
	if c1 not in count2: count2[c1] = {}
	if c2 not in count2[c1]: count2[c1][c2] = 0
	count2[c1][c2] += 1
	#count2[c1][c2] += wordcount[word]

	#  third and alll other letters, given the first two
	for i in range(2, len(word)):
		c1 = word[i-2]
		c2 = word[i-1]
		c3 = word[i]
		if c1 not in count3: count3[c1] = {}
		if c2 not in count3[c1]: count3[c1][c2] = {}
		if c3 not in count3[c1][c2]: count3[c1][c2][c3] = 0
		count3[c1][c2][c3] += 1
		#count3[c1][c2][c3] += wordcount[word]

rs1 = '' # random source for 1st character
for c in count1:
	rs1 += c * count1[c]

rs2 = {} # random source for 2nd character
for c1 in count2:
	if c1 not in rs2: rs2[c1] = ''
	for c2 in count2[c1]:
		rs2[c1] += c2 * count2[c1][c2]

rs3 = {} # random source for 3rd and all other letter
for c1 in count3:
	if c1 not in rs3: rs3[c1] = {}
	for c2 in count3[c1]:
		if c2 not in rs3[c1]: rs3[c1][c2] = ''
		for c3 in count3[c1][c2]:
			rs3[c1][c2] += c3 * count3[c1][c2][c3]

while True:
	word = ''
	c1 = random.choice(rs1)
	c2 = random.choice(rs2[c1])
	word += c1
	word += c2
	for j in range(10):
		c3 = random.choice(rs3[c1][c2])
		if c3 == '*': break
		word += c3
		c1 = c2
		c2 = c3
	if len(word) > 4:
		c1 = word[0].upper()
		print(f'{c1}{word[1:]}')





