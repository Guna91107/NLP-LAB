from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re


def summarize_text(
    sentences,
    cleaned_sentences,
    top_n=3
):

    if not sentences or not cleaned_sentences:
        return [], [], []

    filtered = [
        (s.strip(), c.strip())
        for s, c in zip(sentences, cleaned_sentences)
        if s.strip() and c.strip()
    ]

    if not filtered:
        return [], [], []

    sentences, cleaned_sentences = zip(*filtered)

    sentences = list(sentences)
    cleaned_sentences = list(cleaned_sentences)

    if len(sentences) <= top_n:

        scores = [1.0] * len(sentences)

        return (
            sentences,
            scores,
            list(range(len(sentences)))
        )

    def custom_tokenizer(text):

        tokens = re.findall(
            r'\b\w+\b',
            text.lower(),
            flags=re.UNICODE
        )

        return [
            token
            for token in tokens
            if len(token) > 1
        ]

    try:

        vectorizer = TfidfVectorizer(

            tokenizer=custom_tokenizer,

            token_pattern=None,

            lowercase=True,

            max_features=5000,

            ngram_range=(1, 2)

        )

        tfidf_matrix = vectorizer.fit_transform(
            cleaned_sentences
        )

    except Exception:

        return [], [], []

    if tfidf_matrix.shape[1] == 0:
        return [], [], []

    tfidf_array = tfidf_matrix.toarray()

    sentence_scores = np.mean(
        tfidf_array,
        axis=1
    )

    sentence_lengths = np.array([
        len(custom_tokenizer(sentence))
        for sentence in sentences
    ])

    sentence_lengths[
        sentence_lengths == 0
    ] = 1

    avg_length = np.mean(sentence_lengths)

    length_factor = np.sqrt(
        avg_length / sentence_lengths
    )

    length_factor = np.clip(
        length_factor,
        0.85,
        1.15
    )

    position_factor = np.linspace(
        1.08,
        0.92,
        len(sentences)
    )

    sentence_scores = (
        sentence_scores *
        length_factor *
        position_factor
    )

    min_score = np.min(sentence_scores)

    max_score = np.max(sentence_scores)

    if max_score - min_score > 0:

        sentence_scores = (
            sentence_scores - min_score
        ) / (
            max_score - min_score
        )

    else:

        sentence_scores = np.ones(
            len(sentence_scores)
        )

    ranked_indices = np.argsort(
        sentence_scores
    )[::-1]

    selected_indices = []

    for idx in ranked_indices:

        if len(selected_indices) >= top_n:
            break

        is_duplicate = False

        for selected_idx in selected_indices:

            similarity = cosine_similarity(
                tfidf_matrix[idx],
                tfidf_matrix[selected_idx]
            )[0][0]

            if similarity > 0.70:

                is_duplicate = True
                break

        if not is_duplicate:
            selected_indices.append(idx)

    if len(selected_indices) < top_n:

        for idx in ranked_indices:

            if idx not in selected_indices:

                selected_indices.append(idx)

            if len(selected_indices) >= top_n:
                break

    selected_indices = sorted(selected_indices)

    summary = [
        sentences[i]
        for i in selected_indices
    ]

    return (
        summary,
        sentence_scores.tolist(),
        selected_indices
    )