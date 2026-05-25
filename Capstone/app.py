from flask import Flask, render_template, request
import PyPDF2
from langdetect import detect

from modules.preprocess import preprocess_text
from modules.summarizer import summarize_text
from modules.ner import extract_entities, highlight_entities

from modules.visualization import (
    plot_word_frequency,
    plot_pos_distribution,
    plot_entity_distribution
)

import spacy
import uuid
import re

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    text = request.form.get('text', '').strip()

    file = request.files.get('file')

    sentences = []
    cleaned = []
    summary = []
    combined = []

    entities = []
    highlighted_summary = []

    word_freq = None
    pos_dist = None
    entity_dist = None

    language = "UNKNOWN"

    if file and file.filename != "":

        try:

            filename = file.filename.lower()
            if filename.endswith(".txt"):

                text = file.read().decode(
                    "utf-8",
                    errors="ignore"
                )
            elif filename.endswith(".pdf"):

                pdf_reader = PyPDF2.PdfReader(file)

                extracted_text = ""

                for page in pdf_reader.pages:

                    page_text = page.extract_text()

                    if page_text:
                        extracted_text += page_text + " "

                text = extracted_text
            else:

                return render_template(
                    'result.html',
                    error="Unsupported file type. Please upload TXT or PDF.",
                    text="",
                    sentences=[],
                    cleaned=[],
                    summary=[],
                    combined=[],
                    entities=[],
                    highlighted_summary=[],
                    word_freq=None,
                    pos_dist=None,
                    entity_dist=None,
                    language="UNKNOWN"
                )

        except Exception as e:

            return render_template(
                'result.html',
                error=f"Error reading file: {str(e)}",
                text="",
                sentences=[],
                cleaned=[],
                summary=[],
                combined=[],
                entities=[],
                highlighted_summary=[],
                word_freq=None,
                pos_dist=None,
                entity_dist=None,
                language="UNKNOWN"
            )
    text = re.sub(r'\s+', ' ', text).strip()

    if not text or len(text.split()) < 5:

        return render_template(
            'result.html',
            error="Please enter meaningful text or upload a valid file.",
            text=text,
            sentences=[],
            cleaned=[],
            summary=[],
            combined=[],
            entities=[],
            highlighted_summary=[],
            word_freq=None,
            pos_dist=None,
            entity_dist=None,
            language="UNKNOWN"
        )
    try:

        language = detect(text)

    except:

        language = "unknown"
    if language == "en":

        try:
            doc = nlp(text)

            sentences, cleaned = preprocess_text(text)

            summary, scores, selected_indices = summarize_text(
                sentences,
                cleaned
            )

            combined = list(zip(sentences, scores))

            entities = extract_entities(doc)

            highlighted_summary = [

                highlight_entities(sentence, doc)

                for sentence in summary
            ]

            uid = str(uuid.uuid4())

            word_freq = plot_word_frequency(
                cleaned,
                filename=f"word_freq_{uid}.png"
            )

            pos_dist = plot_pos_distribution(
                doc,
                filename=f"pos_dist_{uid}.png"
            )

            entity_dist = plot_entity_distribution(
                doc,
                filename=f"entity_dist_{uid}.png"
            )

        except Exception as e:

            return render_template(
                'result.html',
                error=f"NLP Processing Error: {str(e)}",
                text=text,
                sentences=[],
                cleaned=[],
                summary=[],
                combined=[],
                entities=[],
                highlighted_summary=[],
                word_freq=None,
                pos_dist=None,
                entity_dist=None,
                language=language.upper()
            )
    else:

        try:
            raw_sentences = re.split(
                r'[.!?।॥\n]+',
                text
            )

            sentences = []
            cleaned = []

            for sentence in raw_sentences:

                sentence = sentence.strip()

                if not sentence:
                    continue

                cleaned_sentence = re.sub(
                    r'[^\w\s\u0900-\u097F]',
                    '',
                    sentence.lower()
                ).strip()

                if cleaned_sentence:

                    sentences.append(sentence)

                    cleaned.append(cleaned_sentence)

            summary, scores, selected_indices = summarize_text(
                sentences,
                cleaned
            )

            combined = list(zip(sentences, scores))

            entities = []

            highlighted_summary = summary

            uid = str(uuid.uuid4())

            word_freq = plot_word_frequency(
                cleaned,
                filename=f"word_freq_{uid}.png"
            )

            pos_dist = None
            entity_dist = None

        except Exception as e:

            return render_template(
                'result.html',
                error=f"Multilingual Processing Error: {str(e)}",
                text=text,
                sentences=[],
                cleaned=[],
                summary=[],
                combined=[],
                entities=[],
                highlighted_summary=[],
                word_freq=None,
                pos_dist=None,
                entity_dist=None,
                language=language.upper()
            )

    return render_template(
        'result.html',

        text=text,

        sentences=sentences,
        cleaned=cleaned,

        summary=summary,
        combined=combined,

        entities=entities,
        highlighted_summary=highlighted_summary,

        word_freq=word_freq,
        pos_dist=pos_dist,
        entity_dist=entity_dist,

        language=language.upper(),

        error=None
    )

if __name__ == '__main__':
    app.run(debug=True)