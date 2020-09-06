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
        keywordSearchResult = getHittingSetListFromKeywordsList(
            'what is a wild animal'.split(),
            kwords)
        self.assertEqual(
            keywordSearchResult,
            [set(), {0, 1}, {0, 1}, {0}, {0, 1}])
        
    def test_GreedySortedListSpansMaxKeywords(self):
        greedySetList = getGreedySortedList_CoveringMaxElementsFirst(
            [set(), {0, 1}, {0, 1}, {0}, {0, 1}])
        self.assertEqual(greedySetList, [(0,4),(1,3)])

    def test_keywordSearch_ReturnsMatchedSentences(self):
        sentencesList = ConvertParagraphToSentenceLists(
                'lion is a wild animal. dog is a pet animal. lion can kill. dog cannot kill'
            )
        wordSearchSet = BuildSearchSetFromSentenceLists(sentencesList)

        MatchedSentences = getKeywordSearchedSentences(sentencesList, wordSearchSet,
            keywords = 'who cannot kill?'.split())
        self.assertEqual(MatchedSentences[0], 'dog cannot kill')

        MatchedSentences = getKeywordSearchedSentences(sentencesList, wordSearchSet,
            keywords = 'who is a wild animal?'.split())
        self.assertEqual(MatchedSentences[0], 'lion is a wild animal')

    def test_SelectAnswerComparingMatchedSentences(self):
        substring = SelectSubStringPerfectlyMatchingFirstOfSentences(
            substrings = ['lion', 'dog'],
            sentencesList = ['lion is a wild animal', 'dog is a pet animal']
        )
        self.assertEqual(substring, 'lion')
            

    def test_MatchesQuestionWithAnswerGivenParagraph(self):
        page = """Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back. 
Which Zebras are endangered?
What is the aim of the Quagga Project?
Which animals are some of their closest relatives?
Which are the three species of zebras?
Which subgenus do the plains zebra and the mountain zebra belong to?
subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain zebra """

        input = page.splitlines()
        paragraph = input[0]
        answersJumbled = input[6]
        questions = input[1:6]

        sentencesList = ConvertParagraphToSentenceLists(paragraph)
        wordSearchSet = BuildSearchSetFromSentenceLists(sentencesList)

        #for question in questions:
        for question in [questions[1]]:
            print("### Question: " +  question)
            answerSentences = getKeywordSearchedSentences(sentencesList, wordSearchSet,
                keywords = question[0:-1].split())
            #print(answerSentences)
            answerSubstring = SelectSubStringPerfectlyMatchingFirstOfSentences(
                substrings = answersJumbled.split(';'), 
                sentencesList = answerSentences
            )
            print("### Answer: " + answerSubstring)
        
        

if __name__ == '__main__':
    unittest.main()
