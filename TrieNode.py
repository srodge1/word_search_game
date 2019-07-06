from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        """
        The constructor for TrieNode object of a Trie
        """
        self.next_characters = defaultdict(TrieNode)
        self.is_end_char = False
