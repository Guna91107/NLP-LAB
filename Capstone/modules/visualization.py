import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from collections import Counter
import re

plt.rcParams['font.family'] = 'Noto Sans Devanagari'

plt.rcParams['font.sans-serif'] = [
    'Noto Sans Devanagari',
    'Mangal',
    'Arial Unicode MS',
    'DejaVu Sans'
]

def clean_words(words):

    cleaned = []

    for word in words:

        word = word.strip().lower()

        if word.isdigit():
            continue

        if len(word) <= 2:
            continue

        cleaned.append(word)

    return cleaned

def plot_word_frequency(
    cleaned_sentences,
    filename="word_freq.png"
):

    words = " ".join(cleaned_sentences).split()

    words = clean_words(words)

    if not words:
        return None

    freq = Counter(words)

    most_common = freq.most_common(10)

    labels = [w for w, _ in most_common]
    values = [c for _, c in most_common]

    plt.figure(figsize=(10, 5))

    plt.bar(labels, values)

    plt.title(
        "Top Words Frequency",
        fontsize=18,
        fontweight='bold'
    )

    plt.xticks(
        rotation=30,
        ha='right'
    )

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    plt.tight_layout()

    path = f"static/{filename}"

    plt.savefig(
        path,
        bbox_inches='tight'
    )

    plt.close()

    return filename

def plot_pos_distribution(
    doc,
    filename="pos_dist.png"
):

    allowed_pos = {
        "NOUN",
        "PROPN",
        "VERB",
        "ADJ"
    }

    pos_counts = Counter([

        token.pos_

        for token in doc

        if token.pos_ in allowed_pos
    ])

    if not pos_counts:
        return None

    labels = list(pos_counts.keys())
    values = list(pos_counts.values())

    plt.figure(figsize=(7, 5))

    plt.bar(labels, values)

    plt.title(
        "POS Tag Distribution",
        fontsize=16,
        fontweight='bold'
    )

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    plt.tight_layout()

    path = f"static/{filename}"

    plt.savefig(
        path,
        bbox_inches='tight'
    )

    plt.close()

    return filename

def plot_entity_distribution(
    doc,
    filename="entity_dist.png"
):

    allowed_labels = {
        "PERSON",
        "ORG",
        "GPE",
        "DATE",
        "CARDINAL"
    }

    ent_counts = Counter([

        ent.label_

        for ent in doc.ents

        if ent.label_ in allowed_labels
    ])

    if not ent_counts:
        return None

    labels = list(ent_counts.keys())
    values = list(ent_counts.values())

    plt.figure(figsize=(7, 5))

    plt.bar(labels, values)

    plt.title(
        "Entity Type Distribution",
        fontsize=16,
        fontweight='bold'
    )

    plt.xticks(rotation=20)

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    plt.tight_layout()

    path = f"static/{filename}"

    plt.savefig(
        path,
        bbox_inches='tight'
    )
    plt.close()

    return filename