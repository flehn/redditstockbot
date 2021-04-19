import praw
import spacy as spacy
import yfinance as yf
from operator import itemgetter

from hoodwink import hoodwink

reddit = praw.Reddit(
    client_id="EiN3kAhvzjMO2g",
    client_secret="MB1siiKvqzMJhhizCK0j7HY3m2xvkw",
    user_agent="<consoleappStockBot>",
)


# New Dic for Stocktickers
post_dict = {}
# Spacy is package for named entity recognition (NER)
nlp = spacy.load('en_core_web_sm')

def countStocks(subreddit):
    counter = 0
    subreddit_name = reddit.subreddit(subreddit)
    #  retrieve all new comments made to the subreddit:
    for comment in subreddit_name.stream.comments():
        if counter == 100:
            break
        #print(comment.body) gibt den ganzen Kommentar aus
        # Check if there is any StockSymbol in the current comment
        print(f'#{comment.author}: ')
        print(f'"{comment.body}"')
        print("---------------")
        counter += 1
        # txt contains the comment
        txt = comment.body
        # doc contains the NER-tagged text
        doc = nlp(txt)
        # The ents attribute of doc contains a list of entities and their respective tags
        for entity in doc.ents:
            print(f"{entity.label_}: {entity.text}")
            print("---------------")
            #If yes, check if Ticker is already added to the Dic and increase value by 1
            if entity.label_ == 'ORG':
                if entity.text in post_dict:
                    post_dict[entity.text] += 1
                else:
                    post_dict[entity.text] = 1

# optinal menu for user input
def menu():
    choice = input('Enter Subreddit Name: ')
    #stock = input('Enter Stock Symbol: ')
    #subreddit = reddit.subreddit(choice)
    while True:
        try:
            #if subreddit.hot():
            countStocks(choice)
            break
        except:
            print("Oops! Not a valid Subreddit")
            break


def differentsubreddits():
    subreddits = ['stocks', 'investing', 'wallstreetbets', 'options']
    for sub in subreddits:
        countStocks(sub)

def printdictionaryentries():
    if not post_dict:
        print("Dic is empty")
    else:
        var = 0
        for key, value in sorted(post_dict.items(), key=itemgetter(1), reverse=True):
            if var == 50:
                break
            print(key, value)
            var += 1


if __name__ == '__main__':
    # menu()
    differentsubreddits()
    printdictionaryentries()

