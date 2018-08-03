
# Count the number of anagrams from this array of strings
# @param strings - the list of strings to find the number of anagrams
# @return - the number of anagrams
def anagram(strings):
	anagrams = 0
	anagram = True
	for string in strings:
		for second_string in strings:
			if string == second_string:
				continue #because we don't want strings that are the exact same
			char_list_one = list(string)
			char_list_one.sort()
			char_list_two = list(second_string)
			char_list_two.sort()
			print '[*] char_list_one: {}'.format(char_list_one)
			print '[*] char_list_two: {}'.format(char_list_two)
			if len(char_list_one) != len(char_list_two):
				continue
			for i in xrange(len(char_list_one)):
				if char_list_one[i] != char_list_two[i]:
					anagram = False
					print '[-] Not an anagram!'
		if anagram:
			print '[+] Anagram!'
			anagrams += 1
	return anagrams


list_of_strings = ['cat', 'tac', 'thac', 'act', 'ball', 'labl']
print anagram(list_of_strings)
