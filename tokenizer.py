import os
import glob  
import csv
from nltk import word_tokenize


## Function to read corpus data
def read_corpus(folderPath):
    fileList = glob.glob(os.path.join(folderPath,'*.txt'))
    text=''
    for filePath in fileList:
        with open(filePath, 'r', encoding='utf-8') as file:
            text += file.read()  #accumulating contents of all files: sabbai file ko content jodeko
    return text

## Function to remove punctuation
def remove_punctuation(text):
    punctuation = ['।',',','-','(',')','.','’','‘']
    for p in punctuation:
        text=text.replace(p,'')
    return text

## Function to remove stopwords
def remove_stopwords(stopwords, text):
    text = ' '.join([word for word in text.split() if word not in stopwords])
    return text

## Function to tokenize
def tokenize():
    folderPath='Nepali_Corpus/Corpus'
    stopWords = './stopword1.txt'
    text=read_corpus(folderPath)
    text=remove_punctuation(text)
    with open(stopWords, 'r', encoding='utf-8') as file:
        stopwords = file.read()
    text=remove_stopwords(stopwords, text)
    spltext= word_tokenize(text)
    return spltext

## Function to write tokenized data to csv file
def write_to_csv(spltext):
    out='nepali_data_set_1.csv'
    with open(out, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Words'])
        for item in spltext:
            csv_writer.writerow([item])

## Main function
def main():
    spltext=tokenize()
    write_to_csv(spltext)

if __name__ == "__main__":
    main()
