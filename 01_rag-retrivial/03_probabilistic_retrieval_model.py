import os
import shutil
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from rank_bm25 import BM25Okapi
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from doc_text import documents
from start_and_tfidf import pre_process
###################################
#  probabilistic retrieval model  # 
###################################
# relevance probability - document is relevant do query
# query terms = terms present in query
# document terms - terms present in document
# BIM) - probabilistic model assuming term relevance is independent

# how it works
# - initial assumptions dataset with relevants and non-relevants and relevants  documents
# - term weights - calculate weights base in frenquency in non relevants and relevants documents
# - score calculation: based on presence of documents
# - ranking: based by relevance score 
# pros: ranking; probabilistic reasoning; adaptability
# limitations: complexity; initial assumptions; data dependency

text = "Sailing in Crotaia between Split and Zadar is Fantastic. This is cool."

# tokenize documents
tokenized_docs=[pre_process(doc) for doc in documents]
print(tokenized_docs)

#initialize bm25 model
bm25=BM25Okapi(tokenized_docs)

#start prob search
query = "croatia sailing"

def search_bm25(query,bm25):
    tokenized_query = pre_process(query)
    doc_scores = bm25.get_scores(tokenized_query)

    return doc_scores

results = search_bm25(query,bm25)


sorted_results = np.argsort(results)[::1]
for i in np.argsort(results)[::1]:
    print(f"Document {i+1}: {documents[i]}")