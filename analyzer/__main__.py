import os
import argparse
import logging
from collections import defaultdict

from gensim.models.doc2vec import Doc2Vec
from analyzer.utils.pg import select_query, load_data
from analyzer.utils.nlp_factory import create_corpus


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    resp = select_query('SELECT ID, TEXT FROM EVENTS')
    corpus = create_corpus(resp)
    model = Doc2Vec.load('./analyzer/utils/models/doc2vec_model')

    for index in range(len(corpus)):
        doc_id = corpus[index].tags
        words = corpus[index].words
        inferred_vector = model.infer_vector(words)
        sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))
        for sim_doc_id, similarity in sims:
            if sim_doc_id != doc_id:
                load_data('INSERT INTO scores (ID, SIM_ID, SIMILARITY) VALUES (%s, %s, %s)', (doc_id, sim_doc_id, similarity))
                if index % 5000 == 0:
                    print('doc_id={}, similar doc_id={}, similarity={}'.format(doc_id, sim_doc_id, similarity))


if __name__ == '__main__':
    main()
