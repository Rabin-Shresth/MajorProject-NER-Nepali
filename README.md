# MajorProject-NER-Nepali

### LEC076 Batch
1. Aishwarya Shrestha (LEC076BCT003)
2. Amrit Kumal (LEC076BCTBCT004)
3. Anup Dumre (LEC076BCT006)
4. Rabin Shrestha (LEC076BCT024)

### 1.   What is Name Entity Recognition (NER) ?
The named entity recognition (NER) is one of the most popular data preprocessing task. It involves the identification of key information in the text and classification into a set of predefined categories. An entity is basically the thing that is consistently talked about or refer to in the text.

NER is the form of NLP.

At its core, NLP is just a two-step process, below are the two steps that are involved:

1. Detecting the entities from the text.

2. Classifying them into different categories 


## MajorProject-NER-Nepali Dataset Preprocessing (Cleaning, Tokenization, Labelling)
We named our project as: **Sabda-NER**
### Sabda-NER

We have prepared human annotated Name Entity Recognition (NER) dataset for Nepali from the corpus data available at https://amitness.com/ml-datasets . We have taken Nepali News Corpus (i.e from Nagarik and Setopati). 

We have used **NLTK** (a toolkit build for working with NLP) for tokenization.

**Highlights**

* Our Sabda-NER covers five named entities - Person Name, Location, Date, Companies
* During our research we found Everest-NER from which we took reference. We will use Everest-NER dataset for training our model for the first phase. Our Sabda-NER dataset will be used as test dataset.
* From our initial research we will be applying BERT model for our NER project.
* Incoming challenges are further to be discussed.