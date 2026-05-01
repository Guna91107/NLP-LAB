from sklearn.feature_extraction.text import CountVectorizer

text = input("Enter text: ")
sentences = text.split(".")

vectorizer = CountVectorizer().fit_transform(sentences)
vectors = vectorizer.toarray()

score = 0
for i in range(len(vectors)-1):
    overlap = sum(min(vectors[i], vectors[i+1]))
    score += overlap

print("Coherence Score:", score)