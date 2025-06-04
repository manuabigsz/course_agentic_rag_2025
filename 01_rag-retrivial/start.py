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

[''.join(pre_process(doc)) for doc in documents]

        
        
