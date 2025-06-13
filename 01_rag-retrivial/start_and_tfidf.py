import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from doc_text import documents


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


text = "Sailing in Crotaia between Split and Zadar is Fantastic. This is cool."

# tokenize into sentences
#a sentence is defined when there is a "." and an empty space after
print(nltk.sent_tokenize(text))

# tokenize into words
print(nltk.word_tokenize(text))

# pre processing
    # we dont capitalize. i would query "croating sailing" and not "Croating Sailing"
    # croatia is different tha Croacia - they must to be the same!!
    # we dont realy add pontuation and stop words in queries
    
#remove the capitalization
def pre_process(text):
    text_lower = text.lower()

    #tokenize into words
    tokens = nltk.word_tokenize(text_lower)

    return [word for word in tokens if word.isalnum()]

preprocessed_docs = [''.join(pre_process(doc)) for doc in documents]

        
## TF-IDF
vectorizer = TfidfVectorizer()
## regardless of size, they will have 360 ​​dimensions 

# fit and transforme the pre preprocessed docs
tfidf_matrix = vectorizer.fit_transform(preprocessed_docs)
print(f"the shape of tf-ifdf matrix id {tfidf_matrix}")
print(f"the lenght of documents is {len(documents)}")

## query the index
query = "croatia sailing"
query_vectorizer = vectorizer.transform([query])

## measures or helps to measure the distances (cosines) between a query and dimensions
## sort the documents by similaritie to the query
similarities = cosine_similarity(tfidf_matrix, query_vectorizer)
sorted_similarities = list(enumerate(similarities))
sorted_similarities = sorted(sorted_similarities, key=lambda x: x[1])

# function to search with tf-idf
def search_tfidf(query, vectorizer,tfidf_matrix):
    query_vec = vectorizer.transform([query])
    
    similarities = cosine_similarity(tfidf_matrix, query_vec).flatten()
    
    #pair each document index with its siilartiry score:
    sorted_similarities = list(enumerate(similarities))
    
    results = sorted(sorted_similarities, key=lambda x: x[1])
    
    return results

search_similarities = search_tfidf(query, vectorizer, tfidf_matrix)

print("top 10 docments by similarity score for query {query}:")
for doc_index, score in search_similarities[:10]:
    print(f"Document {doc_index + 1}: {documents[doc_index]}")
    
    
    
