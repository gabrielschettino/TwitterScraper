
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("722x473")
window.configure(bg = "#70E0DE")

def Busca():
    print("teste")

def BuscaTweets():
    query = entry_1.get()
    nomecsv = entry_2.get()
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
    df.to_csv(nomecsv + ".csv")


canvas = Canvas(
    window,
    bg = "#70E0DE",
    height = 473,
    width = 722,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    361.0,
    0.0,
    722.0,
    473.0,
    fill="#BFF5F4",
    outline="")

canvas.create_text(
    408.0,
    193.99999999999994,
    anchor="nw",
    text="Insira o nome do arquivo de saida .csv:",
    fill="#000000",
    font=("JostRoman Regular", 16 * -1)
)

canvas.create_text(
    33.0,
    35.99999999999994,
    anchor="nw",
    text="Twitter Scraper",
    fill="#000000",
    font=("JostRoman Regular", 40 * -1)
)

canvas.create_text(
    408.0,
    73.99999999999994,
    anchor="nw",
    text="Insira a Query de busca do Twitter:",
    fill="#000000",
    font=("JostRoman Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    539.0,
    131.49999999999994,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=420.0,
    y=105.99999999999994,
    width=238.0,
    height=49.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    539.0,
    267.49999999999994,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=420.0,
    y=241.99999999999994,
    width=238.0,
    height=49.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: BuscaTweets(),
    relief="flat"
)
button_1.place(
    x=403.0,
    y=365.99999999999994,
    width=272.0,
    height=51.0
)
window.resizable(False, False)
window.mainloop()