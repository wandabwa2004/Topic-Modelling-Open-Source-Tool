import pandas as pd
import gensim
def lda_train(corpus,id2word,number_of_topics=5):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=number_of_topics, 
                                           random_state=2020,
                                           update_every=1,
                                           chunksize=10,
                                           passes=10,
                                           alpha='symmetric',
                                           iterations=100,
                                           per_word_topics=True)
    return lda_model


