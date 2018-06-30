# run this for an interactive cmd line
# python w2v_cmd_line.py

# this script tries to save model with L2, to avoid having to calc L2 on each run.
#
# - but the resulting file is about 8.7Gb which cannot be subsequently loaded on my laptop.
# think this would require data streaming or else partitioning across machines...

import code
import gensim
import os.path

# from manually unzipping
MODEL_FILE = "D:\\big_data\\w2v_googlenews_zipped\\GoogleNews-vectors-negative300.bin\\GoogleNews-vectors-negative300.bin"

# from this script (to speed up subsequent runs)
MODEL_WITH_L2 = "D:\\big_data\\w2v_googlenews_zipped\\GoogleNews-vectors-negative300.bin\\GoogleNews-vectors-negative300.bin.l2"

hasL2 = os.path.isfile(MODEL_WITH_L2)

if hasL2:
    print("loading model from " + MODEL_WITH_L2 + " (has L2 norms)")
    model = gensim.models.word2vec.Word2Vec.load(MODEL_WITH_L2)
else:
    print("loading model from " + MODEL_FILE)
    model = gensim.models.word2vec.Word2Vec.load_word2vec_format(MODEL_FILE, binary=True)
    print("replacing with l2 norms (euclidean distance between word vectors?)")
    model.init_sims(replace=True)
    print("saving model with L2 norms")
    # note: saving a word2vec model in gensim format fails on load, due to this issue:
    #   https://github.com/RaRe-Technologies/gensim/issues/525
    model.save_word2vec_format(MODEL_WITH_L2)

print('model.similarity("sweden", "france")')

print(model.similarity("sweden", "france"))

code.interact(local=locals())
