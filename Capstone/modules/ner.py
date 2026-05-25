import spacy

nlp = spacy.load("en_core_web_sm")

ALLOWED_ENTITY_LABELS = {
    "PERSON",
    "ORG",
    "GPE",
    "DATE"
}

BLOCKED_TERMS = {

    # technical phrases
    "cloud computing",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "ai",
    "the years",
    "llc",
    "inc",
    "ltd",
    "corp",
    "co"
}

BLOCKED_SHORT_WORDS = {
    "a",
    "an",
    "the"
}

def extract_entities(doc):

    seen = set()

    entities = []

    for ent in doc.ents:

        if ent.label_ not in ALLOWED_ENTITY_LABELS:
            continue

        text = ent.text.strip()

        lower_text = text.lower().strip(".")

        if lower_text in BLOCKED_TERMS:
            continue

        if lower_text in BLOCKED_SHORT_WORDS:
            continue

        if len(text) <= 2:
            continue

        if text.isupper() and len(text) <= 3:
            continue

        if len(text.split()) > 3:
            continue

        key = (text, ent.label_)

        if key not in seen:

            seen.add(key)

            entities.append({
                "text": text,
                "label": ent.label_
            })

    return entities

def highlight_entities(sentence, doc):

    result = sentence

    already_done = set()

    ents = sorted(
        doc.ents,
        key=lambda x: len(x.text),
        reverse=True
    )

    for ent in ents:

        if ent.label_ not in ALLOWED_ENTITY_LABELS:
            continue

        text = ent.text.strip()

        lower_text = text.lower().strip(".")

        if lower_text in BLOCKED_TERMS:
            continue

        if lower_text in BLOCKED_SHORT_WORDS:
            continue

        if len(text) <= 2:
            continue

        if text.isupper() and len(text) <= 3:
            continue

        if len(text.split()) > 3:
            continue

        if text in already_done:
            continue
        if text in result:

            highlighted = (
                f"<span style='background-color:yellow;'>"
                f"{text} ({ent.label_})"
                f"</span>"
            )

            result = result.replace(
                text,
                highlighted,
                1
            )

            already_done.add(text)

    return result