import re
import nltk
import gensim
import logging

from pymystem3 import Mystem
from string import punctuation
from nltk.corpus import stopwords


log = logging.getLogger(__name__)

def clean_html(text: str) -> str:
    regexp = re.compile('<.*?>|[a-zA-Z]+|&|;')
    return re.sub(regexp, '', text)

def preprocess_text(text: str, mystem: Mystem, stopwords: stopwords) -> list:
    text = clean_html(text)
    tokens = mystem.lemmatize(text.lower())

    return [token for token in tokens if token not in stopwords\
            and token != " " \
            and token.strip() not in punctuation \
            and token not in [' «', '» ']]

def create_corpus(texts: list) -> list:
    corpus = []
    prep_texts = []
    mystem = Mystem()
    try:
        russian_stopwords = stopwords.words("russian")
    except:
        nltk.download('stopwords', download_dir='./analyzer/utils/cache')
        russian_stopwords = stopwords.words("russian")

    for id, text in texts:
        prep_texts.append(preprocess_text(text, mystem, russian_stopwords))
    log.info('Cleaned and lemmatized texts')

    for index, text in enumerate(prep_texts):
        corpus.append(gensim.models.doc2vec.TaggedDocument(text, texts[index][0]))
    log.info('Created taggeddocument (corpus)')

    return corpus






