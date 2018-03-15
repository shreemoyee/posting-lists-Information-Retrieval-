
# coding: utf-8

# In[54]:

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile, join



mypath="/home/shreemoyee/Desktop/Assign02_IR/20_newsgroups/comp.graphics"
f=listdir(mypath)
doc_freq={}
term_freq={}
for i in range(0,len(f)):
      if isfile(join(mypath,f[i])):
            doc=open(join(mypath,f[i]))
            t=doc.read()
            print(i)
            #print(t)
            doc.close()
            words = word_tokenize(t)
            stop=set(stopwords.words("english"))
            punc=['.','""',"''",' ','``','?','-',',']
            filtered_words=[word.lower() for word in words]
            filtered_words = [word for word in filtered_words if word.isalpha()]
            filtered_words=[word for word in filtered_words if not word in stop]
            filtered_words=[word for word in filtered_words if not word in punc]

            
            tf={}
            for w in filtered_words:
                if w in tf.keys():
                    tf[w]+=1
                else:
                    
                    tf[w]=0
                if w in doc_freq.keys():
                        
                        doc_freq[w].append(f[i])
                else:
                        doc_freq[w]=[]
                        #print(w)
                        doc_freq[w].append(f[i])
            term_freq[f[i]]=tf





# In[132]:

import csv
with open('/home/shreemoyee/Desktop/Assign02_IR/document_freq.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in doc_freq.items():
        writer.writerow([key, value])


# In[135]:

with open('/home/shreemoyee/Desktop/Assign02_IR/term_freq.txt', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in term_freq.items():
         writer.writerow([key, value])
df=pd.DataFrame(columns=term_freq.keys())
df['words']=doc_freq.keys()


# In[105]:

df=df.set_index('words')
df['words']=doc_freq.keys()

# In[121]:

df['words'].shape[0]


# In[126]:

for i in range (0,len(df.columns)):
    print(i)
    for j in range(0,df['words'].shape[0]):
        if df['words'][j] in term_freq[df.columns[i]].keys():
            df[df.columns[i]][df['words'][j]]=term_freq[df.columns[i]][df['words'][j]]
        else:
            df[df.columns[i]][df['words'][j]]=0




df=df.drop(['words'],axis=1)



df.to_csv('/home/shreemoyee/Desktop/Assign02_IR/posting_list.csv')






