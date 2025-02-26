#!/usr/bin/env python
import sys
import collections

# ----------------------------------------------------------------------------------------
#	This reducer code will input a <word, value> input file, and join words together
# 	Note the input will come as a group of lines with same word (ie the key)
# 	As it reads words it will hold on to the value field
#
# 	It will keep track of current word and previous word, if word changes
#   	then it will perform the 'join' on the set of held values by merely printing out 
#   	the word and values.  In other words, there is no need to explicitly match keys b/c
#   	Hadoop has already put them sequentially in the input 
#   
# 	At the end it will perform the last join
#
#
#  	Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   	it has word with correct and matching entries, no extra spaces, etc.
#
#  	see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  	San Diego Supercomputer Center copyright
# ----------------------------------------------------------------------------------------

prev_word = " "
line_cnt = 0  # count input lines
kv = { }
lstword = []
val = 0
abc_found = False

sys_stdin = sys.stdin

for line in sys_stdin:
    line =  line.strip() # strip out carriage return
    key_value = line.split('\t') # split line, into key and value, returns a list
    line_cnt = line_cnt + 1

    curr_word = key_value[0]
    value_in = key_value[1]   

    if value_in.upper() == 'ABC':
	abc_found = True
	value_in = 0 	
    
    # index = len(lstword)

    if curr_word not in lstword:        
        lstword.append(curr_word)
     
    if curr_word in lstword:
	val = val + int(value_in)
	# print curr_word, value_in, val, len(lstword), index
	kv[curr_word] = val

# for word in lstword:
    # print word

# print lstword

# print kv

skv = (sorted(kv.items()))

# for k in skv:
    # print skv[0], skv[1]

for index in range(len(skv)):
    #print index
    #print skv[index][0], skv[index][1]
    if index == 0:
	print skv[index][0], skv[index][1]
    elif index > 0:
	print skv[index][0], (skv[index][1] - skv[index - 1][1])





