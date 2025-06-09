import os
import shutil
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from doc_text import documents

#############################
#  boolean retrieval model  # 
#############################
#      and - or - not       #
#############################
# steps:
# 1. tokenization
# 2. normalization - convertng to lower case, remove pontuantion, etc
# 3. inverted index created - mapping terms
# 4. query processing - retrivial of matching documents
# pros: its simplicity and precision
# limitations: no ranking, binary matching (no middleground), complex queries
text = "Sailing in Crotaia between Split and Zadar is Fantastic. This is cool."


# pre processing part 2
def pre_process2(text):
    text_lower = text.lower()

    #tokenize into words
    tokens = nltk.word_tokenize(text_lower)
    
    # list the tokens per document
    tokes = [word for word in tokens if word.isalnum()]
    
    # remove the stop words
    stopwords = set(nltk.corpus.stopwords.words('english') - {"and", "or", "not"})
    tokens = [word for word in tokens if word not in stopwords]
    
    return tokens

print(text)
text_processed = pre_process2(text)
print(text_processed)

