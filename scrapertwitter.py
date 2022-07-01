import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
from tkinter import *

root = Tk()
labelquery = Label(root, text = "Insira a Query de pesquisa avançada do Twitter:")
labelarq = Label(root, text = "Insira nome do arquivo de saída:")
botaorodar = Button(root, text="Buscar")

labelquery.grid(row=0, column=0)
labelarq.grid(row=1, column=1)
botaorodar.grid(row=3, column=0)

root.mainloop()



def BuscaTweets(query, nomecsv):
    query = query
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
    df.to_csv(nomecsv)