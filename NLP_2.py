
""" NAME: NIHARIKA PENTAPATI
    SRN: PES1201700215
"""

from __future__ import print_function
from __future__ import absolute_import

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import operator
import nltk

# nltk.download('wordnet')

porter_stemmer = PorterStemmer()
wordnet_lemm = WordNetLemmatizer()

# print(type(wordnet_lemm))

file = 'result1.txt'

filename = open(file, 'r')
all_words = filename.read()
sent_tokenize_list = sent_tokenize(all_words)
word_tokenize_list = word_tokenize(all_words)
print('Sentenced Tokenized List:', sent_tokenize_list)
print()
print('Word Tokenized List:', word_tokenize_list)
print()

stop_words = stopwords.words('english')
w_list = word_tokenize_list.copy()
for word in word_tokenize_list:
    if word.lower() in stop_words:
        w_list.remove(word)
print('List after removing stop words:', w_list)
print()
word_freqs = Counter(w_list)
print('Frequency of words after removal of stop words:', word_freqs)
print()

w_list1 = []
for word in word_tokenize_list:
    w_list1.append(porter_stemmer.stem(word))
print('Words after stemming:', w_list1)
print()

w_list2 = []
for word in word_tokenize_list:
    w_list2.append(wordnet_lemm.lemmatize(word))
print('Words after lemmatization:', w_list2)
print()

pos = nltk.pos_tag(word_tokenize_list)
print('Part of speech tagging:', pos)
print()

w_list3 = []
w_list4 = []
for sentence in sent_tokenize_list:
    w_list3 = word_tokenize(sentence)
    w_list4.append(w_list3)

w_dict5 = {}
i = 0
for _list in w_list4:
    freq_dict = Counter(_list)
    _sum = sum(freq_dict.values())
    w_dict5[i] = _sum
    i = i+1
print('Dictionary of sentence index and its frequency:', w_dict5)
print()

x = w_dict5
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print('List of sorted tuples with sentence index and it frequency:', sorted_x)
print()

print('Top ten sentences with maximum frequency:')
print()

for i in range(10):
    num = sorted_x[i][0]
    print(sent_tokenize_list[num])
    print()
    print("(END OF SENTENCE)")
    print()
