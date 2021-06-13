import os
import argparse
import logging

from gensim.models.doc2vec import Doc2Vec
from analyzer.utils.pg import select_query, load_data, pg_cursor
from analyzer.utils.nlp_factory import create_corpus

SQL_QUERY_FOLDER = './analyzer/utils/sql/{}.sql'
MODEL_FILE_NAME = './analyzer/utils/models/doc2vec_model'


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    load_query = open(SQL_QUERY_FOLDER.format('load_data'), 'r').read()
    insert_query = open(SQL_QUERY_FOLDER.format('insert_score'), 'r').read()

    resp = select_query(load_query)
    corpus = create_corpus(resp)
    model = Doc2Vec.load(MODEL_FILE_NAME)

    for index in range(len(corpus)):
        doc_id = corpus[index].tags
        words = corpus[index].words
        inferred_vector = model.infer_vector(words)
        sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))

        with pg_cursor() as cur:
            for sim_doc_index, similarity in sims[:30]:
                if sim_doc_index != doc_id:
                    sim_doc_id = corpus[sim_doc_index].tags
                    cur.execute(insert_query, (doc_id, sim_doc_id, similarity, None))
                    if index % 5000 == 0:
                        print('doc_id={}, similar doc_id={}, similarity={}'.format(doc_id, sim_doc_id, similarity))


if __name__ == '__main__':
    main()
