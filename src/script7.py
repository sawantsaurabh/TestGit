import re, math
from collections import Counter
import pandas as pd
import cProfile

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

##############################################
xl = pd.ExcelFile("new_topic_mapping.xlsx")
df = xl.parse("Sheet1")
#df = df.head(n=50)

#print df
text2= df['value'].str.lower()
#print text2
topics=df['topic']




text1 = 'brach information mahim'
#text2 = ['This sentence is similar to a foo bar sentence .','Hello hw r u']
# text2 = 'This sentence is similar to a foo bar sentence .'

# vector1 = text_to_vector(text1)
# print("vector1 : ",vector1)
#vector2 = text_to_vector(text2)
#print vector2
# vector1 = text1
# print vector1
# vector2 = text2

# cosine = get_cosine(vector1, vector2)
# print 'Cosine',cosine 
#print map(text_to_vector(),text2)
data12=[]
all_data=[]

def final_score():
    for vec in text2:
        abc=text_to_vector(vec)
        data12.append(abc)
    
    for text_2_all in data12:
        final_data=get_cosine(text_to_vector(text1), text_2_all)
        all_data.append(final_data)
    print(all_data)
    
    all_list = pd.DataFrame(
        {'Score': all_data,
         'Sentences': text2,
         'lst3Tite': data12,
         'Topic':topics
         
        })
    sorted_list=all_list.sort(['Score'], ascending=[False])
    print sorted_list.head(n=10)

#var1 = cProfile.run('final_score()')
#print(var1)
#print all_list.sort(['lst1Tite'], ascending=[False])
final_score()

