# Python Code for CS 170
import sys
import fileinput

# basic set-up
max_result = -1
content = []
for line in fileinput.input():
    line = line.strip()
    content.append(line)


class Matches:
	def __init__(self, first, second, value):
		self.first = first
		self.second = second
		self.value = value

# Dynamic Programming SubString Finder
def substringfinder(X, Y, m, n):
	substring_matrix_list = [[0 for x in xrange(n + 1)] for x in xrange(m + 1)]
	result = 0
	i = 0
	j = 0
	while (i <= m):
		while (j <= n):
			if (i == 0 or j == 0):
				substring_matrix_list[i][j] = 0;
			elif (X[i - 1] == Y[j - 1]):
				substring_matrix_list[i][j] = substring_matrix_list[i - 1][j - 1] + 1;
				result = max(result, substring_matrix_list[i][j])
			else:
				substring_matrix_list[i][j] = 0;
			j += 1
		i += 1
		j = 0
	if (X[len(X) - result:] == Y[:-(len(Y) - result)]):
		return result
	if (Y[len(Y) - result:] == X[:-(len(X) - result)]):
		return result
	else:
		return 0;

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


# Calculates all the overlaps for all the strings
def mostoverlaps(content):
	global max_result
	values = None
	i = 0
	j = 0
	while (i < len(content)):
		while (j < len(content)):
			if (i < j):
				first = content[i].strip()
				second = content[j].strip()
				tmp_result = substringfinder2(first, second)
				# print tmp_result
				if (tmp_result != 0):
					indicator = Matches(i, j, tmp_result);
				# print indicator
				if (tmp_result > max_result):
					max_result = tmp_result
					values = indicator
			j += 1
		i += 1
		j = i
	return values

# Combiner for all the overlaps found
def combinator(content):
	global max_result
	max_result = 0
	values = mostoverlaps(content)
	if (values):
		seq1 = content[values.first].strip()
		seq2 = content[values.second].strip()
		combined = substring_edge(seq1, seq2, max_result)
		if (combined is None):
			combined = substring_edge(seq2, seq1, max_result)
		if (combined):
			content[values.first] = combined
			del content[values.second]
		return combined
	return

def substring_edge(seq1, seq2, max_result):
	if (seq1 == seq2):
		return seq1
	if (seq1.find(seq2) > -1):
		return seq1
	if (seq1[len(seq1) - max_result:] == seq2[:-(len(seq2) - max_result)]):
		return seq1 + seq2[max_result:]
	return

# mostoverlaps(content)
combined = "filler"
while (combined is not None):
	combined = combinator(content)

print content[0]
