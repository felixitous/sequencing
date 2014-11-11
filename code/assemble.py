import sys
import fileinput

content = []
for line in fileinput.input():
    line = line.strip()
    content.append(line)

# Regular Finder for Substring
def substringfinder2(X, Y):
	farthest_check = min(len(X), len(Y))
	# base case
	if (X == Y):
		return farthest_check
	if (X.find(Y) > -1):
		return len(Y)
	elif (Y.find(X) > -1):
		return len(X)
	longest_substring = 0
	result = 1
	while (result <= farthest_check):
		if X[len(X) - result:] == Y[:-(len(Y) - result)]:
			longest_substring = result
		elif Y[len(Y) - result:] == X[:-(len(X) - result)]:
			longest_substring = result
		result += 1
	return longest_substring

#clear duplicates
def duplicate_clear(content):
	i = 0
	j = 0
	while (i < len(content)):
		while (j < len(content)):
			if (i < j):
				first = content[i]
				second = content[j]
				if first in second:
					del content[i]
				elif second in first:
					del content[j]
			j += 1
		i += 1
		j = 1
	return content


# Calculates all the overlaps for all the strings
overlap_values = {}
def mostoverlaps(content):
	global overlap_values
	max_result = 0
	winner1 = None
	winner2 = None
	i = 0
	j = 0
	while (i < len(content)):
		while (j < len(content)):
			if (i < j):
				first = content[i]
				second = content[j]
				key = first + "|" + second
				tmp_result = overlap_values.get(key)
				if tmp_result is None:
					tmp_result = substringfinder2(first, second)
				overlap_values.update({key : tmp_result})
				if tmp_result > max_result:
					max_result = tmp_result
					winner1 = first
					winner2 = second
			j += 1
		i += 1
		j = 0
	combined = substring_edge(winner1, winner2, max_result)
	if combined is None:
		combined = substring_edge(winner2, winner1, max_result)
	content.remove(winner1)
	content.remove(winner2)
	content.append(combined)
	return content

def substring_edge(seq1, seq2, max_result):
	if (seq1 == seq2):
		return seq1
	if (seq1.find(seq2) > -1):
		return seq1
	if (seq1[len(seq1) - max_result:] == seq2[:-(len(seq2) - max_result)]):
		return seq1 + seq2[max_result:]
	return

content = duplicate_clear(content)
while (len(content) > 1):
	content = mostoverlaps(content)
print content[0]
