import sys
import time
import string
import random

from Trie import Trie
from WordSearch import WordSearch


def main():
    words_dictionary = Trie()
    file_name = sys.argv[1]
    lowercase_letters = string.ascii_lowercase
    try:
        with open(file_name, 'r') as file_handle:
            for word in file_handle:
                words_dictionary.insert_word(word.rstrip())
    except:
        pass

    word_search_game = WordSearch(words_dictionary)

    while True:
        cmd = int(input("Enter 1 to play else any other digit to exit! : "))
        if cmd == 1:
            num_rows = int(input("Please enter number of rows for the grid : "))
            num_cols = int(input("Please enter number of columns for the grid : "))
            start = time.time()
            grid = [[random.choice(lowercase_letters) for i in range(num_cols)]
                    for j in range(num_rows)]

            print('\n')
            for row in grid:
                print(row)

            print(word_search_game.search_valid_words(grid))
            print("\n",time.time()-start,"\n")

        else:
            sys.exit()


if __name__ == "__main__":
    main()
