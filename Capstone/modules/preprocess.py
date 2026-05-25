import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):

    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words('english'))
    cleaned_sentences = []

    for sentence in sentences:
        sentence_lower = sentence.lower()

        sentence_clean = sentence_lower.translate(
            str.maketrans('', '', string.punctuation)
        )

        words = word_tokenize(sentence_clean)

        filtered_words = [
            lemmatizer.lemmatize(w)
            for w in words
            if w not in stop_words
            and w.isalpha()         # remove numbers
            and len(w) > 2          # remove very short words
        ]

        cleaned_sentences.append(" ".join(filtered_words))

    return sentences, cleaned_sentences