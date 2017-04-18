#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:38:17 2017

@author: oliver
"""
import string
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return (float)(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
    return (float)(math.log(len(bloblist)) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return (float)(tf(word, blob)) * (float)(idf(word, bloblist))



def deformat(bloblist):
    for c in string.punctuation:
        bloblist=bloblist.replace(c," ")
        bloblist=bloblist.lower()
    return bloblist

with open("combined.txt", 'r') as myfile:
    txt=myfile.read().replace('\n', '')
q=tb(txt)
r = deformat(q)
print r
bloblist = [r]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
