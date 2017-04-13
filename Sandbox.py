import os
import shutil
import math
from text.blob import TextBlob as tb # Note: I eventually didn't use this
import string

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def deformat(word, bloblist):
    for c in string.punctuation:
        bloblist=bloblist.replace(c,"")
        bloblist=bloblist.lower()
    return bloblist


filenames = []

thing = 0

outfilename = "C:/Users/Oliver/Desktop/LIS590AG_Assignment6/combined.txt"

for root, dirs, files in os.walk('C:/Users/Oliver/Desktop/LIS590AG_Assignment6/NSF_Part1'):
    for file in files:
        if file.endswith(".txt"):
            filenames.append(os.path.join(root, file))
            with open(outfilename, 'wb') as outfile:
                for filename in filenames:
                    if filename == outfilename:
                        continue
                    with open(filename, 'rb') as readfile:
                        shutil.copyfileobj(readfile, outfile)

wordlist = "C:/Users/Oliver/Desktop/LIS590_Assignment6/combined.txt"

deformat(wordlist)
tf(wordlist)
n_containing(wordlist)
idf(wordlist)


