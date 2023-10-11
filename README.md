# Twitter-COVID19-Sentimental-Analysis
## Objectives and Business Value:
This project conducts sentiment analysis on COVID-19-related Twitter posts in Canada, aiming to understand public sentiment on topics like vaccines and travel restrictions. The endeavor holds significant value as it offers real-time insights into public sentiments, allowing public health organizations to tailor effective communication strategies and policies. For businesses, this analysis enables them to adjust services and marketing efforts according to public sentiment, while media outlets can report on trending topics. In summary, this sentiment analysis provides valuable insights with applications spanning public health, business strategies, research, and media engagement, facilitating the alignment of policies, services, and content with the public's views and concerns.

## Analysis Procedure:
During our study, we collected and filtered 1000 COVID-related tweets from Canada using specific keywords and categorized them into eight topics, also annotating their sentiment (negative, positive, or neutral). The dataset was carefully collected using the Twitter API and Tweepy, from November 25th to 27th, 2021. Data collection criteria included avoiding retweets and ensuring each tweet contained COVID-related keywords. The study also employed randomization to minimize the impact of outlier tweets. Cleaned data led to the identification of eight distinct topics, including advertisement, measures, politics, public opinions, research, statistics, travel, and vaccine. The study computed the TF-IDF scores for relevant words in each topic, leading to a list of top-10 words for each category, revealing the most relevant terms for each. After finding the most relevant terms, we were able to identify the general sentiment towards different topics related to COVID-19, particularly focusing on hot topics in Canada.

## Files uploaded:
- **get_tweets.py:** This script connects to the Twitter API and retrieves 1000 tweets containing specific COVID-related keywords. It then saves the results in a CSV file named 'tweets.csv'.

- **analysis.py:** In this script, each tweet from the 'tweets.csv' file is processed. It removes all stopwords to obtain unique words and stores the cleaned data in a new CSV file called 'redefined_tweets.csv'.

- **Results_Tweets.xlsx:** This Excel file comprises two sheets. One contains all the cleaned tweets with manual annotations, while the other includes pivot tables and graphs used in the final report.

- **tfidf.py:** This script reads tweets from the 'tweets.csv' file and performs a TF-IDF word analysis for unique words within each category.

- **Final_report.pdf:** This document presents the comprehensive report for the project.

## Statement of Contribution:
This project was conducted as a collaborative effort within a group of three members, with all team members contributing equally at every stage of the project.
