from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "NLP is fun",
    "I love natural language processing",
    "Information retrieval uses TF IDF"
]

query = ["natural language"]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + query)

scores = cosine_similarity(tfidf[-1], tfidf[:-1])

print("Document Rankings:")
for i, score in enumerate(scores[0]):
    print(f"Document {i+1} -> Score: {score}")
