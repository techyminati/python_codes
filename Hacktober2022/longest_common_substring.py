# Function to find Longest Common Sub-string

from difflib import SequenceMatcher

def longestSubstring(str1,str2):

	# initialize SequenceMatcher object with
	# input string
	seqMatch = SequenceMatcher(None,str1,str2)

	# find match of longest sub-string
	# output will be like Match(a=0, b=0, size=5)
	match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

	# print longest substring
	if (match.size!=0):
		print (str1[match.a: match.a + match.size])
	else:
		print ('No longest common sub-string found')

# Driver program
if __name__ == "__main__":
	str1 = 'GeeksforGeeks'
	str2 = 'GeeksQuiz'
	longestSubstring(str1,str2)
