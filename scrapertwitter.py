import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv

query = "(from:jairbolsonaro) since:2020-01-01"
tweets = []
limit = 15000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url, tweet.replyCount, tweet.retweetCount, tweet.likeCount])
        
df = pd.DataFrame(tweets, columns=['Data', 'Username', 'Tweet', 'URL', 'Respostas', 'Retweets', 'Likes'])
print(df)

#salvando para csv
df.to_csv('tweetsjairbolsonaro.csv')