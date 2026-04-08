import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["running", "flies", "better", "studies"]

ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in words]

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)
print("Lemmatized words:", lemmatized_words)