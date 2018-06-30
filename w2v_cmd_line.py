# run this for an interactive cmd line
# python w2v_cmd_line.py

import code
import gensim

MODEL_FILE = "D:\\big_data\\w2v_googlenews_zipped\\GoogleNews-vectors-negative300.bin\\GoogleNews-vectors-negative300.bin"


print("loading model from " + MODEL_FILE)

model = gensim.models.word2vec.Word2Vec.load_word2vec_format(MODEL_FILE, binary=True)

print("replacing with l2 norms (euclidean distance between word vectors?)")
model.init_sims(replace=True)

print('model.similarity("sweden", "france")')

print(model.similarity("sweden", "france"))

code.interact(local=locals())
