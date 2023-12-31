# Knesset Analysis

A final project for the "Dynamic Networks and NLP" course, by Guy Barel and Gal Astrach.

Explanation of the code:

## 'Scraping/oknesset_scraping.py'
Contains the code to get the data from open knesset.

## `/nlp`
- Contains a jupyter notebook with the code for generating the figures that are in the article.
- Contains `sentiment.py` that adds the sentiment column to the dataset.

## The dataset
To run the pipeline that mines the data, clean it and adds the sentiment you can:
1. run `Scraping/oknesset_scraping.py`.
2. run `nlp/sentiment.py` on its output.

The data is already pre-made inside the **Setup** section in the notebook where we download it from Dropbox.
