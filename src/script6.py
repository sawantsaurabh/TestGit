from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import pandas as pd 
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    #print wn_tag 
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def path_sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    #print 'sentence1',sentence1
    #print 'sentence2',sentence2
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    #print "synsets1",synsets1
    synsets2 = [ss for ss in synsets2 if ss]
    #print "synsets2",synsets2
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
        #print best_score
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score
###################################################################################
def lch_sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    #print 'sentence1',sentence1
    #print 'sentence2',sentence2
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    #print "synsets1",synsets1
    synsets2 = [ss for ss in synsets2 if ss]
    #print "synsets2",synsets2
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.lch_similarity(ss) for ss in synsets2])
        #print best_score
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score
#####################################################################################
def wup_sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    #print 'sentence1',sentence1
    #print 'sentence2',sentence2
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    #print "synsets1",synsets1
    synsets2 = [ss for ss in synsets2 if ss]
    #print "synsets2",synsets2
    score, count = 0.0, 0
 
    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = max([synset.wup_similarity(ss) for ss in synsets2])
        #print best_score
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score




############################################### 
# sentences = [
#     "Dogs are awesome.",
#     "Some gorgeous creatures are felines.",
#     "Dolphins are swimming mammals.",
#     "Cats are beautiful animals.",
# ]
# 
#  
# focus_sentence = "Cats are beautiful animals."
##############################################
xl = pd.ExcelFile("new_topic_mapping.xlsx",nrows=50)
df = xl.parse("Sheet1")
df = df.head(n=50)
print df
sentences= df['value']
print sentences
topics=df['topic']
################################################
# sentences = [
# "ATM Address",
# "ATM City",
# "ATM launch date",
# "ATM Machine Type",
# "ATM RBI Class",
# "ATM Region",
# "ATM State",
# "ATM other Bank Transactions Orange Metro V/s Edge SA",
# "ATM other Bank Transactions Orange Non-Metro V/s Nova SA",
# "ATM other Bank Transactions Zwipe v/s Pro SA",
# "ATM Zing V/s Junior SA",
# "Branch ATM for"    
# ]

focus_sentence = "information regarding transaction orange metro other atm banks"
#focus_sentence = "Revised Sweepin limit"
for sentence in sentences:
    
        print "path_Similarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, path_sentence_similarity(focus_sentence, sentence))
#    print "path_Similarity(\"%s\", \"%s\") = %s" % (sentence, focus_sentence, path_sentence_similarity(sentence, focus_sentence))
     
#     print "lch_Similarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, lch_sentence_similarity(focus_sentence, sentence))
#     print "lch_Similarity(\"%s\", \"%s\") = %s" % (sentence, focus_sentence, lch_sentence_similarity(sentence, focus_sentence))
 
#    print "wup_Similarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, wup_sentence_similarity(focus_sentence, sentence))
#    print "wup_Similarity(\"%s\", \"%s\") = %s" % (sentence, focus_sentence, wup_sentence_similarity(sentence, focus_sentence))

# Similarity("Cats are beautiful animals.", "Dogs are awesome.") = 0.511111111111
# Similarity("Dogs are awesome.", "Cats are beautiful animals.") = 0.666666666667
 
# Similarity("Cats are beautiful animals.", "Some gorgeous creatures are felines.") = 0.833333333333
# Similarity("Some gorgeous creatures are felines.", "Cats are beautiful animals.") = 0.833333333333
 
# Similarity("Cats are beautiful animals.", "Dolphins are swimming mammals.") = 0.483333333333
# Similarity("Dolphins are swimming mammals.", "Cats are beautiful animals.") = 0.4
 
# Similarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0
# Similarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0

def symmetric_path_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (path_sentence_similarity(sentence1, sentence2) + path_sentence_similarity(sentence2, sentence1)) / 2 

# def symmetric_lch_sentence_similarity(sentence1, sentence2):
#     """ compute the symmetric sentence similarity using Wordnet """
#     return (lch_sentence_similarity(sentence1, sentence2) + lch_sentence_similarity(sentence2, sentence1)) / 2 
# 
# 
# def symmetric_wup_sentence_similarity(sentence1, sentence2):
#     """ compute the symmetric sentence similarity using Wordnet """
#     return (wup_sentence_similarity(sentence1, sentence2) + wup_sentence_similarity(sentence2, sentence1)) / 2 

path_result_list=[]
lch_result_list=[]
wup_result_list=[]

for sentence in sentences:

#     print "Path_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#     focus_sentence, sentence, symmetric_path_sentence_similarity(focus_sentence, sentence))
        
        abc=focus_sentence, sentence, symmetric_path_sentence_similarity(focus_sentence, sentence)

#     print "Path_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#         sentence, focus_sentence, symmetric_path_sentence_similarity(sentence, focus_sentence))
    
#     print "LCH_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#         focus_sentence, sentence, symmetric_lch_sentence_similarity(focus_sentence, sentence))
#     xyz=focus_sentence, sentence, symmetric_lch_sentence_similarity(focus_sentence, sentence)
#     print "LCH_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#         sentence, focus_sentence, symmetric_lch_sentence_similarity(sentence, focus_sentence))
     
#     print "WUP_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#         focus_sentence, sentence, symmetric_wup_sentence_similarity(focus_sentence, sentence))
#     pqr=focus_sentence, sentence, symmetric_wup_sentence_similarity(focus_sentence, sentence)
#     print "WUP_SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
#         sentence, focus_sentence, symmetric_wup_sentence_similarity(sentence, focus_sentence))
 
        path_result_list.append(abc)
#    lch_result_list.append(xyz)
#    wup_result_list.append(path_result_list)

print path_result_list
labels = ['A', 'B', 'C','D']
path_df = pd.DataFrame.from_records(path_result_list, columns=labels)
print path_df.sort(['C'],ascending=[False])
print path_df.shape
# lch_df = pd.DataFrame.from_records(lch_result_list, columns=labels)
# print lch_df.sort(['C'],ascending=False)
# print lch_df.shape

#wup_df = pd.DataFrame.from_records(wup_result_list, columns=labels)
#print wup_df.sort(['C'],ascending=False)
#print wup_df.shape
#df1=path_df.append(lch_df)
# df1=path_df
# df2=df1.append(wup_df)
# print "df2",df2.sort(['C'],ascending=False)
# df2.drop_duplicates(cols = 'C', inplace = True)
# SymmetricSimilarity("Cats are beautiful animals.", "Dogs are awesome.") = 0.588888888889
# SymmetricSimilarity("Dogs are awesome.", "Cats are beautiful animals.") = 0.588888888889
 
# SymmetricSimilarity("Cats are beautiful animals.", "Some gorgeous creatures are felines.") = 0.833333333333
# SymmetricSimilarity("Some gorgeous creatures are felines.", "Cats are beautiful animals.") = 0.833333333333
 
# SymmetricSimilarity("Cats are beautiful animals.", "Dolphins are swimming mammals.") = 0.441666666667
# SymmetricSimilarity("Dolphins are swimming mammals.", "Cats are beautiful animals.") = 0.441666666667
 
# SymmetricSimilarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0
# SymmetricSimilarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0
 