_end ='$'

def make_trie(*words):
	root = dict()
	for word in words:
		current_node = root
		for letter in word:
			current_node = current_node.setdefault(letter,{})
		current_node[_end] = _end
	return root

words =["apple","orrange","apply","ranger","ape"]
root = make_trie(words)

print root


