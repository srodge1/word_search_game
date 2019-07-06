# word_search_game

To play the word search game, clone the repo and run python main.py <filename> <br />
To run the unittests python test_unittest.py

# Requirements :
1] Windows OS <br />
2] Python 3.6.5 <br />

# Trie.py :
Implements Trie data structure.

# WordSearch.py :
Implements WordSearch class. After receiving words_dictionary and grid it performs dfs(Depth First Search) algorithm on the grid and finds out all the valid words. A valid word is the one present in the words_dictionary. These valid are returned in the form of a list.

# test_unittest.py :
For testing both Trie class and WordSearch class.

# main.py :
Implements the driver code. Reads words from the filename provided as command line input and creates Trie data structure out of it. <br />
Trie increases perfomance for word searching while efficiently managing memory. That's why I chode this data sctructure. <br />
On running main.py you will be prompted to choose size of the character grid i.e. number of rows and number of columns. This code will generate that sized grid with random characters from a-z, for that I have used string and random modules.<br />
List of valid words returned will be printed along with time it took for execution from forming the grid and getting the valid words out of it.
