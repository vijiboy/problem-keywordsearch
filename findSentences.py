def ConvertParagraph_To_ListOfLists(text):
    if not text or not isinstance(text, str) or not text.strip():
        raise ValueError("invalid or empty text")
    textSentences = []
    for para in (text.splitlines()):
        for sentence in para.split(". "):
            if not sentence.strip(): continue
            textSentences.append(sentence.split())
    return textSentences
                                
