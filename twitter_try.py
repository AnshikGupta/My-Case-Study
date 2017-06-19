from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentence_sentiment as ss

#consumer key, consumer secret, access token, access secret.
ckey="21xTOFchecEWHWK3H4doaskRq"
csecret="X4oX7ZmmtTniH9JVmKqyCUkSubUbvjKCE0VRkrRwhPEOR8iNK4"
atoken="872740170952564736-eanFHqgjzeDKPnUnpie0256N7vvh0pv"
asecret="WVTZrY4EAtAkVmFFsPboqifOFtmojrTxh53tNL708Z4uE"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sentiment_value = ss.sent_analysis(tweet)
        tweet = tweet.encode("utf-8", errors='ignore')
        print(tweet,sentiment_value)

        output = open("twitter-out.txt","a")
        output.write(sentiment_value)
        output.write('\n')
        output.close()
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])

