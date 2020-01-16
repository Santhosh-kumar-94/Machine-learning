from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import sentiment_module as senti

ckey="yDkLNYoBhLAKOkhbeh3QEz3rH"
csecret="kg1kOH5qivdnYqLYeLssP3djE75dpMIXOOBRecDwpEc10D70wC"
atoken="1215144892147482624-9am8QFN9HEqAYwPryAVWiGPMXC6Q4i"
asecret="Tq7qTkTRMUo2kxkdqNR2mjzrvpyxIwFg32s4FZnbiUwiL"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value,confidence = senti.sentiment(tweet)
            print (tweet, sentiment_value,confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(tweet)
                output.write(" "+sentiment_value)
                output.write('\n')
                output.close()
            

            return True
        except:
            return True

    def on_error(self, status):
        print(status)
        


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["confident"])
