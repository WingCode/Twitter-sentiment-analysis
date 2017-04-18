#################################
from operator import itemgetter
import sys

sentence=""
word_list=[]
for line in sys.stdin:
    line = line.strip()
    count, word = line.split('\t', 1)
    word_list.append(str(word))

str1= ' '.join(word_list)
print str1
#####################################

import csv
sentences=[]
sentis=[]
i=0
temp=[]
import pydoop.hdfs as hdfs
with hdfs.open('/senti/train.csv') as f:
    spamreader = csv.reader(f,delimiter=',')
    for row in spamreader:
        if row[0]=='negative':
            sentis.append(-1)
        elif row[0]=='neutral':
            sentis.append(0)
        elif row[0]=='positive':
            sentis.append(1)
        sentences.append(row[1])

uniq=[]
for i in sentences:
    uniq.extend(i.split())

uniq=list(set(uniq))


import numpy as np
vector_space=np.zeros((len(sentences),len(uniq)))


i=0
while(i<4):
    j=0
    while j<len(uniq):
        if uniq[j] in sentences[i].split():
            vector_space[i][j]=1
        j+=1
    i+=1


from sklearn import svm
clf=svm.SVR(C=1.0)
sentis=np.asarray(sentis)
clf.fit(vector_space,sentis)

pred=str1
vect_pred=np.zeros(len(uniq))
i=0
while i<len(uniq):
    if uniq[i] in pred.split():
        vect_pred[i]=1
    i+=1
#print(vect_pred)


result_final=clf.predict(vect_pred)
print '%s\t%s' % ("1", str(result_final))