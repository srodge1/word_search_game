import unittest

from Trie import Trie
from WordSearch import WordSearch


class Test(unittest.TestCase):
    def test_trie(self):
        words_dictionary = Trie()
        words = ["zoro", "luffy", "sanji", "nami", "brook", "jimbei", \
                "luf", "bro", "jim", "san"]
        for word in words:
            words_dictionary.insert_word(word)

        for word in words:
            self.assertTrue(words_dictionary.search_word(word))

        self.assertFalse(words_dictionary.search_word("sa"))
        self.assertFalse(words_dictionary.search_word("zor"))
        self.assertFalse(words_dictionary.search_word("sand"))
        self.assertFalse(words_dictionary.search_word("jimb"))
        self.assertFalse(words_dictionary.search_word("name"))
        self.assertFalse(words_dictionary.search_word("game"))

    def test_word_search(self):
        words_dictionary = Trie()
        words = ["naruto", "naru", "leemo", "hokage", "leaf", "sakura", \
                "saskent", "kiba", "lee", "noji", "leen"]
        for word in words:
            words_dictionary.insert_word(word)
        word_search_game = WordSearch(words_dictionary)

        grid = [['n', 'j', 'r', 'u'],
                ['o', 'a', 'i', 't'],
                ['l', 'e', 'o', 'p'],
                ['e', 'n', 'm', 'q']]

        valid_words = set(["noji", "naru", "naruto", "lee", "leen", "leemo"])
        ret_words = word_search_game.search_valid_words(grid)
        for word in ret_words:
            if word in valid_words:
                valid_words.remove(word)
            else:
                valid_words.add(word)

        self.assertEqual(len(valid_words), 0)


if __name__ == "__main__":
    unittest.main()
