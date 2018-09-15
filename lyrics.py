import nltk
from urllib import request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file1 = open('C:\\Users\\Desktop\\girl_like_you.txt' ,'r')
lyrics = file1.read()
lyrics = lyrics.split('\n')


for lyric in lyrics:
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(lyric)
    print(lyric)
    print(scores)
