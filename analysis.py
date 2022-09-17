import re
import string
import pandas as pd

def get_stops():
    with open("stopwords.txt","r") as f:
        stops = f.readlines()
    stops = stops[6:]
    for i in range(len(stops)):
        stops[i] = (stops[i]).strip()
    return stops

def remove_stops(line,stops):
    for s in stops:
        s = str.lower(s)
        while(s in line):
            line.remove(s)
    return line

def check_chars(word):
    for letter in word:
        val = ord(letter)
        if ((not (65 <= val <= 90)) and (not (97 <= val <= 122)) and (not (48 <= val <= 57))):
            return False
    return True

def clean(stops, review):  
    splitted = review.split(" ")
    li = []
    for i, word in enumerate(splitted):
        if (len(word) != 0):
            if ((not "https://" in word) and (word[0] != '#') and (word[0] != '@')):
                li.append(word.lower())
    new_review = ' '.join(li)
    table = str.maketrans('','',string.punctuation)
    review = new_review.translate(table)
    review = review.split(" ")
    li2 = []
    for w in review:
        if (check_chars(w) and (not w.isdigit())):
            li2.append(w)
    return remove_stops(li2,stops)

def main():
    stops = get_stops()
    df = pd.read_csv("tweets.csv")
    df = df.drop(columns=['date', 'Unnamed: 0'])
    for i in range(df.shape[0]):
        modif = (clean(stops, df.iloc[i,0]))
        df.iloc[i,0] = " ".join(modif)
    df.to_csv("refined_tweets.csv")

if __name__=="__main__":
    main()