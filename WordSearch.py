class WordSearch():
    """
    The class for creating word search game using words dictionary
    """
    def __init__(self, words_dictionary):
        """
        The constructor to initiate word search game object.

        Parameters:
            words_dictionary(Trie): Dictionary for searcing words.
        """
        self.words_dictionary = words_dictionary

    def search_valid_words(self, grid):
        """
        The function to search valid words(from words.txt file) that can be
        formed from given character array grid.

        Parameters:
            grid(List[List[str]]): grid of [a-z] characters to form words.

        Returns:
            result(List[str]): list of valid words formed in grid.
        """
        self.result = []
        if not grid:
            return self.result

        self.visiting = [[False for j in range(len(grid[0]))] \
                            for i in range(len(grid))]
        root = self.words_dictionary.root
        # To avoid duplecates, could reduce performance but improves reusability
        self.found_words = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] not in root.next_characters:
                    continue
                self.__get_valid_words(root, grid, row, col, "")

        return self.result

    def __get_valid_words(self, node, grid, row, col, part_word):
        print(part_word)
        if node.is_end_char:
            # On finding the end character, invalidating it would make words
            # dictionary vulnerable for consecutive searches
            if part_word not in self.found_words:
                self.result.append(part_word)
                self.found_words.add(part_word)

        if (row < 0) or (row >= len(grid)) or (col < 0) or \
            (col >= len(grid[0])) or self.visiting[row][col]:
            return
        self.visiting[row][col] = True

        cur_char = grid[row][col]
        node = node.next_characters.get(cur_char)
        if not node:
            self.visiting[row][col] = False
            return

        for r, c in ((0,1), (0,-1), (1,0), (-1,0), (1,1), \
                        (-1,1), (1,-1), (-1,-1)):
            self.__get_valid_words(node, grid, row+r, col+c,
                            part_word+cur_char)

        self.visiting[row][col] = False
