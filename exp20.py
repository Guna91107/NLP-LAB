from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "I love machine learning",
    "NLP is interesting",
    "I love coding in python"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

query = input("Enter query: ")
q_vec = vectorizer.transform([query])

scores = (X * q_vec.T).toarray()

for i, score in enumerate(scores):
    print("Doc", i+1, "Score:", score[0])