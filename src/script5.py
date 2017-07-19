from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn

# dog = wn.synset('dog.n.01')
# cat = wn.synset('cat.n.01')

#dog = wn.synset('charge.n.01')
#cat = wn.synset('fee.n.01')

dog= wn.synsets('atm','n')[2]     # Get the most common synset

#print dog
#print dog.lemmas()

cat = wn.synsets('transaction','n')[0]

#print cat

#print dog.path_similarity(cat)

#print dog.lch_similarity(cat)

#print dog.wup_similarity(cat)

from nltk.wsd import lesk
sent = 'I went to bank for atm transaction money.'
#sent = 'atm enviromental problem.'

ambiguous = 'atm'
#dog= wn.synsets('atm','n')[2]
print wn.synsets('atm','n')[1]
#print lesk(sent, ambiguous)
#print lesk(sent, ambiguous).definition()
#########################################################
from pywsd.lesk import simple_lesk
from pywsd.lesk import adapted_lesk
from pywsd.lesk import original_lesk
sent = 'I went to the atm to deposit my money'
ambiguous = 'atm'
answer = simple_lesk(sent, ambiguous, pos='n')
answer1 = adapted_lesk(sent, ambiguous, pos='n')
#answer2 = original_lesk(sent, ambiguous, pos='n')
#print answer
#print answer.definition()

#print answer1
#print answer1.definition()

#print answer2
#print answer2.definition()

##########################################################

from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim


print maxsim('I want atm address','atm', 'lch')
#print disambiguate('I went to the atm to deposit my money')
#print disambiguate('atm deposit money', algorithm=maxsim, similarity_option='wup', keepLemmas=True)
#print disambiguate('regarding ATM money transaction', algorithm=maxsim, similarity_option='path', keepLemmas=False)


#from pywsd.similarity import max_similiarity
#print max_similarity('my cat likes to eat mice', 'cat', 'wup', pos='n').definition 
##########################################################
import sense2vec
model = sense2vec.load()
#sense2vec.download()
#text="natural_language_processing|NOUN"
text="atm |NOUN"
freq, query_vector = model[text.decode()]
print model.most_similar(query_vector, n=3)

print get_taxonomy('atm')
