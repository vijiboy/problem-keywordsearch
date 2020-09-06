import unittest
from findSentences import *
import os

class Test_TextStructuring(unittest.TestCase):
    def test_ConvertParagraph_To_SentenceLists(self):
        #print(ParseParagraph("single sentence"))
        sentences = ConvertParagraphToSentenceLists("single sentence")
        self.assertEqual(len(sentences), 1)
        self.assertEqual(sentences[0], ['single', 'sentence'])

        for text in [ "first sentence. and second. ",
                      "\nfirst sentence. and second. ",
                      "first sentence. and second. \n",
                      "   first sentence.   and second.   ",
                      ". first sentence. and second.  " ] :
            sentences = ConvertParagraphToSentenceLists(text)
            self.assertEqual(len(sentences), 2)
            self.assertEqual(sentences[0], ['first', 'sentence'])
            self.assertEqual(sentences[1], ['and', 'second'])

    def test_InvalidParagraph_Raises_ValueError(self):
        with self.assertRaises(ValueError):
            ConvertParagraphToSentenceLists("")
        with self.assertRaises(ValueError):
            ConvertParagraphToSentenceLists("\n")

    def test_ConvertSentencesToSet(self):
        searchSet = BuildSearchSetFromSentenceLists(
            ConvertParagraphToSentenceLists(
                "first line. second line"))
        self.assertEqual(searchSet, {'first':{0}, 'line':{0,1}, 'second': {1}})

    def test_RetriveSentences_WithMaxMatchesFirst(self):
        slist = ConvertParagraphToSentenceLists(
            "lion is a wild animal. dog is a pet animal")
        kwords = BuildSearchSetFromSentenceLists(
            slist)
        keywordSearchResult = getSentencesSetsFromKeywords(
            'what is a wild animal'.split(),
            kwords)
        print(keywordSearchResult)

        

if __name__ == '__main__':
    unittest.main()
