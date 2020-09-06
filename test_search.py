import unittest
from findSentences import *
import os

class Test_TextStructuring(unittest.TestCase):
    def test_ConvertParagraph_To_ListOfLists(self):
        #print(ConvertParagraph_To_ListOfLists("first sentence. and second.  "))
        sentences = ConvertParagraph_To_ListOfLists("first sentence. and second. ")
        self.assertEqual(sentences[0], ['first', 'sentence'])
        self.assertEqual(sentences[1], ['and', 'second'])


if __name__ == '__main__':
    unittest.main()