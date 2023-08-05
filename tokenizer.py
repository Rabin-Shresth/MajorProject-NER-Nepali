## Corpus data bata csv ma convert garne (Tokenizer)

import nltk
import os
import glob  
import csv
from nltk import word_tokenize


folderPath='Nepali_Corpus/Corpus'

fileList = glob.glob(os.path.join(folderPath,'*.txt'))

text=''

for filePath in fileList:
    with open(filePath, 'r', encoding='utf-8') as file:
         text += file.read()  #accumulating contents of all files: sabbai file ko content jodeko


punctuation = ['।',',','-','(',')','.']

for p in punctuation:
    text=text.replace(p,'')

spltext= word_tokenize(text)


# print(spltext)

out='dataset_opt.csv'

with open(out, 'w', newline='', encoding='utf-8-sig') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Words'])
    for item in spltext:
        csv_writer.writerow([item])


# print(l)