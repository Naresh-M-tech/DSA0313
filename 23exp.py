from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')

text = """Natural language processing is interesting.
It is a branch of artificial intelligence.
Bananas are yellow."""

sentences = nltk.sent_tokenize(text)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(sentences)

scores = []
for i in range(len(sentences)-1):
    score = cosine_similarity(tfidf[i], tfidf[i+1])[0][0]
    scores.append(score)

print("Coherence Scores:", scores)
print("Average Coherence:", sum(scores)/len(scores))
