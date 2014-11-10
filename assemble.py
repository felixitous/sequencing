# Python Code for CS 170
import sys
import fileinput

# basic set-up
max_result = -1
# arguments = list(sys.argv)
# file_name = arguments[1]
# sequences = open(file_name, "r")
# content = sequences.readlines()
content = []

for line in fileinput.input():
	content.append(line.strip())


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
overlap_values = {}
def mostoverlaps(content):
	global max_result
	global overlap_values
	values = None
	i = 0
	j = 0
	while (i < len(content)):
		while (j < len(content)):
			if (i < j):
				first = content[i].strip()
				second = content[j].strip()
				tmp_result = substringfinder2(first, second)
				overlap_values.update({ (i, j) : tmp_result})
				# print tmp_result
				# if (tmp_result != 0):
				# 	indicator = Matches(i, j, tmp_result);
				# # print indicator
				# if (tmp_result > max_result):
				# 	max_result = tmp_result
				# 	values = indicator
			j += 1
		i += 1
		j = i
	return

# Combiner for all the overlaps found
def combinator(content):
	global overlap_values
	removes = 0
	max_value = 0
	key_value = None
	# print overlap_values
	for key in overlap_values:
		# print overlap_values[key]
		if (max_value < overlap_values[key]):
			# print overlap_values[key]
			max_value = overlap_values[key]
			key_value = key

	# values = mostoverlaps(content)
	# if (values):
	print key_value
	if (key_value):
		# print key_value[0]
		seq1 = content[key_value[0]].strip()
		seq2 = content[key_value[1]].strip()
		combined = substring_edge(seq1, seq2, max_value)
		if (combined is None):
			combined = substring_edge(seq2, seq1, max_value)
		if (combined):
			content[key_value[0]] = combined
			print content[key_value[0]]
			print content[key_value[1]]
			print combined
			# print combined
			# del overlap_values[]
			# del overlap_values[(values.first, values.second)]
			# if (len(content) > 1):
			accu_recal(key_value, combined)
			# del content[values.second]
			# removes += 1
			# print key_value[0]
			return key_value[0]
		else:
			return 0
	return
	# return

def accu_recal(values, combined):
	global overlap_values
	# print overlap_values
	for key in overlap_values:
		if overlap_values[key] == 0:
			continue
		# overlap_values[key] = 0
		elif values[0] == key[0] and values[1] == key[1]:
			overlap_values[key] = 0
		elif values[0] == key[0]:
			seq1 = content[key[1]].strip()
			# print combined
			# print seq1
			tmp_result = substringfinder2(combined, seq1)
			overlap_values[key] = tmp_result
		elif values[0] == key[1]:
			seq1 = content[key[0]].strip()
			# print combined
			# print seq1
			tmp_result = substringfinder2(combined, seq1)
			overlap_values[key] = tmp_result
		elif values[1] == key[0]:
			overlap_values[key] = 0
			# tmp = key[1]
			# seq1 = content[tmp].strip()
			# tmp_result = substringfinder2(combined, seq1)
			# overlap_values[key] = tmp_result
		elif values[1] == key[1]:
			overlap_values[key] = 0
			# seq1 = content[key[0]].strip()
			# tmp_result = substringfinder2(combined, seq1)
			# overlap_values[key] = tmp_result
		# else:


def substring_edge(seq1, seq2, max_result):
	if (seq1 == seq2):
		return seq1
	if (seq1.find(seq2) > -1):
		return seq1
	if (seq1[len(seq1) - max_result:] == seq2[:-(len(seq2) - max_result)]):
		return seq1 + seq2[max_result:]
	return

# mostoverlaps(content)
combined = 0
mostoverlaps(content)
counter = 0
while (counter < len(content)):
	temp = combinator(content)
	if (temp is not None):
		combined = temp
	else:
		break
		# break
	counter += 1

print temp
print overlap_values
# print content
# print combined
print content[combined]

# first = "GGGTCATCTGCCTACCGATTT"
# second = "GGGTCATCTGCCTACCGATTTTATGAGAAAGTCCTTTGCA"
# print substringfinder3(first, second)
# print substring_edge(second, first, 21)
# print len(second)
# print substringfinder2(first, second)
