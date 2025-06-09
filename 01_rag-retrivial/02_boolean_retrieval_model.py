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

if(os.path.exists("index_dir")):
    shutil.rmtree("index_dir")
os.mkdir("index_dir")

schema = Schema(title=ID(stored = True, unique=True,), content = TEXT(stored = True))

index = create_in("index_dir", schema)

# add doc by writing to the index
writer = index.writer()
for i, doc in enumerate(documents):
    writer.add_document(title = str(i), content=pre_process2(doc))
writer.commit()

#query using boleean
query = "croacia NOT sailing"

# queryparser that targets the content field
parser = QueryParser("content", schema = index.schema)

#parser the users query
parsed_query = parser.parse(query)
print(f"parsed query: {parsed_query}")
with index.searcher() as searcher:
    results = searcher.search(parsed_query)
    print([[hit["title"], hit['content']] for hit in results])

#build function for boolean search
def boolean_search(query, index):
    parser = QueryParser("content", schema = index.schema)

    parsed_query = parser.parse(query)
    print(f"parsed query: {parsed_query}")
    with index.searcher() as searcher:
        results = searcher.search(parsed_query)
     
        return [[hit["title"], hit['content']] for hit in results]


boolean_search(query, index)


