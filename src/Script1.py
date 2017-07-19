import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

#text1 = 'ATM Dadar address .'
#text1 = 'ATM Bandra address '
#text2 = 'Dadar address ATM .'
#text2 = 'ATM Dadar address .'

#text1='A quick brown dog jumps over the lazy fox.'
#text2='A quick brown fox jumps over the lazy dog.'

text1='It is a dog'
text2='It is a log'

#text2 = 'ATM Dadar address .'
#text1 = ' want  any Dadar address for ATM .'


vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print 'Cosine:', cosine