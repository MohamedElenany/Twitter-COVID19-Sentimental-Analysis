# Twitter-COVID19-Sentimental-Analysis
## About:
The aim of the project is to understand the Canadian reaction on COVID related topics like vaccine and travel restrictions; this is achieved by conducting sentimental analysis on COVID19 related twitter posts in Canada. In a group with two other members, we used the twitter API to collect 1000 english tweets (within a three day window) that contain specific key-words related to COVID, then we conducted an open coding session on a portion of them to specify the topics we will focus on. After that, we manually annotated the rest of them. Finally, we used the TF-IDF methodology in order to find the words with the highest score in each category, which helped us in building a general sentiment towards each topic.

## Files uploaded:
-> get_tweets.py :  a script used to connect to the twitter API and collect 1000 tweets that contain specific COVID rekated keywords, then save the results in a csv file, 'tweets.csv'

-> analysis.py: a script used to iterate through all tweets in the tweets.csv file, clean each line from all stopwords (in order to get only unique words) from the stopwords.txt file, then output the result in a csv, 'redefined_tweets.csv'

-> Results_Tweets.xlsx: the excel file contains one sheet with all the cleaned tweets with our manual annotations beside each tweet, and another sheet with some pivot tables and graphs used in the final report.

-> tfidf.py: a script that reads all tweets from tweets.csv file and, for each category, it prints a tfidf word analysis on unique words in tweets

-> Final_report.pdf: contains the full report for the project

