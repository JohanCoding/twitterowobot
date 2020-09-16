import tweepy
 
print("running")
api_key = " " #put your keys
api_secret = " " #put your keys
coolacesstoken = " " #put your keys
coolacesssecret = " " #put your keys
userid = " " #the person you want to reply to twitter id
twitterhandle = "@____" #Persons twitter handle
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(coolacesstoken, coolacesssecret)
api =  tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.user.id != int(userid):
            return
        elif not status.retweeted and 'RT @' not in status.text:
            print(f"They Tweeted: {status.text}")
            message = status.text
            message = message.replace("brother", "onii-chan")
            message = message.replace('L', 'W')
            message = message.replace('R', 'W')
            message = message.replace('l', 'w')
            message = message.replace('r', 'w')
            message = message.replace("no", "nyo")
            message = message.replace("mo", "myo")
            message = message.replace("No", "Nyo")
            message = message.replace("Mo", "Myo")
            message = message.replace("na", "nya")
            message = message.replace("They", "Dey")
            message = message.replace("they", "dey")
            message = message.replace("them", "dem")
            message = message.replace("ni", "nyi")
            message = message.replace("nu", "nyu")
            message = message.replace("ne", "nye")
            message = message.replace("anye", "ane")
            message = message.replace("inye", "ine")
            message = message.replace("onye", "one")
            message = message.replace("onye", "one")
            message = message.replace("Josh", "Jwosh")
            message = message.replace("josh", "Jwosh")
            message = message.replace("Jawsh", "Jwoshy")
            message = message.replace("The ", "Da ")
            message = message.replace("Hi ", "Haiii <3")
            message = message.replace("Hello", "Hewwo ")
            message = message.replace(":)", "– ̗̀ (ᵕ꒳ᵕ) ̖́ –")
            message = message.replace("Hi ", "Haiii<3 ")
            message = message.replace("you ", "youwu ")
            api.update_status("Hewwo, " + message, in_reply_to_status_id = status.id, auto_populate_reply_metadata = True)
            print(f"You Replied {message}")
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[userid])
