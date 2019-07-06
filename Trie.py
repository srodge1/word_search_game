from TrieNode import TrieNode


class Trie(object):
    """
    This is a class for constructing words dictionary in Trie data structure.
    """
    def __init__(self):
        """
        The constructure for Trie class.
        """
        self.root = TrieNode()

    def insert_word(self, word):
        """
        The function to insert word into trie.

        Parameters:
            word(str): word to be inserted into trie.

        Returns:
            None(NoneType)
        """
        node = self.root
        for char in word:
            node = node.next_characters[char]
        node.is_end_char = True

    def search_word(self, word):
        """
        The function to search word in the trie.

        Parameters:
            word(str): word to be searched in the trie

        Returns:
            (bool): True if word present in trie else false
        """
        node = self.root
        for char in word:
            node = node.next_characters.get(char)
            if not node:
                return False

        return node.is_end_char
