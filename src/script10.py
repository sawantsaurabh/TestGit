from gensim.models import Doc2Vec
fn = "word_vectors_blog_post_v01_notes"
print fn
model = Doc2Vec.load(fn)
model.most_similar('pregnant')
matches = list(filter(lambda x: 'SENT_' in x[0], matches))

def get_vector(word):
    return model.syn0norm[model.vocab[word].index]
def calculate_similarity(sentence, word):
   vec_a = get_vector(sentence)
   vec_b = get_vector(word)
   sim = np.dot(vec_a, vec_b)
   return sim
calculate_similarity('SENT_47973, 'casual')
