def ConvertParagraphToSentenceLists(text):
    ''' parse and convert text to sentence lists '''
    if not text or not isinstance(text, str) or not text.strip():
        raise ValueError("invalid or empty text")
    SentenceLists = []
    sentenceEnd = ". " # sentence defined as string ending with dot then space
    for para in (text.splitlines()):
        for sentence in para.split(sentenceEnd): 
            if not sentence.strip(): continue
            SentenceLists.append(sentence.split())
    return SentenceLists

def BuildSearchSetFromSentenceLists(SentenceLists):
    ''' builds a map (Hitting Set) of words to their sentences '''
    wordSearchSet = {} # maps word to sentences its present in
    for sindex, sentence in enumerate(SentenceLists):
        for word in sentence:
            if word not in wordSearchSet: wordSearchSet[word] = set()
            wordSearchSet[word].add(sindex)
    return wordSearchSet

def getHittingSetListFromKeywordsList(keywords, wordSearchSet):
    ''' get sentence indexes given keyword(s) '''
    hittingSetList = []
    for word in keywords:
        hittingSetList.append(
            set() if word not in wordSearchSet else wordSearchSet[word])
    return hittingSetList

def getGreedySortedList_CoveringMaxElementsFirst(hittingSetList):
    if not hittingSetList: raise ValueError("hittingSetList invalid or empty")
    greedyListWithCount = []
    MaxCountList = []
    for hs in hittingSetList:
        MaxCountList.extend(hs)
    from collections import Counter
    greedyListWithCount = Counter(MaxCountList).most_common()
    return greedyListWithCount
    

def getKeywordSearchedSentences(text, keywords):
    ''' given keywords, returns best match sentences list '''
    sentencesList = ConvertParagraphToSentenceLists(text)
    wordSearchSet = BuildSearchSetFromSentenceLists(sentencesList)
    hittingSetList = getHittingSetListFromKeywordsList(
        keywords, wordSearchSet)
    SearchedSentenceIndexes = getGreedySortedList_CoveringMaxElementsFirst(
        hittingSetList)
    return [' '.join(sentencesList[sIndex]) for sIndex,repeatCount in SearchedSentenceIndexes]


    
