def summarizer(text):
    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation

    # List of stop words
    stopwords = list(STOP_WORDS)
    # pass document into spacy and store in "doc" object
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    #print(tokens)

    #List item
    # add \n to the punchuvation list
    punctuation = punctuation + '\n' + '\n\n'
    punctuation

    # Preparing a dictionary for word frequencies¶
    word_frequencies = {}                       # Dictionary Name
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():   
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] +=1
        #print(word_frequencies)
      #  if word_frequencies.values:
       #     max_frequency = max(word_frequencies.values(),default=1)

    # Normalize the word frencies
    #for word in word_frequencies.keys():
     #   word_frequencies[word] = word_frequencies[word]/max_frequency
     
    #sentence tokenization -Calculate sentences scores¶   By creating a Dictionay for sentences and its normalized frequencies
    sentence_tokens = [sent for sent in doc.sents]
    #print(sentence_tokens)
    sentence_scores = {}                                            #create Dictionary
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():        
                if sent not in sentence_scores.keys():              # add word normalized frequencies count in each of these sentences,then with maximum value we are going to find important sentence 
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    sentence_scores

    # Can tweek percentage
    # Get 30% of important sentences with maximum score - using nlargest
    from heapq import nlargest
    select_length = int(len(sentence_tokens)*0.2)
    select_length
    summary = nlargest(select_length , sentence_scores , key = sentence_scores.get)
    summary   # Got 4 important sentences
    final_summary = [word.text for word in summary]
    final_summary
    #print(len(final_summary))
    #combining above 4 lines togeather to from a summary
    summary = ' ' .join(final_summary)
    summary
    summary1 = summary.replace('\n', ' ')

    print('\n')
   # print("Text summarization using SPACY")
    print(summary1)
   # print('\n')
   # print("length of original text:",len(text))
   # print("length of autosummarization text using SPACY",len(summary))

