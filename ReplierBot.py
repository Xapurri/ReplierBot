
import tweepy, time
#Access
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def automsg():    #Generates an automatic reply
    
    message= 'message' #message to send to the person who has sent a Tweet
    toReply = 'user' #Without the @
    api = tweepy.API(auth)
    
    
    # Gets the id of the last tweet in order to recognize if there is a new tweet or not
    tweets = api.user_timeline(screen_name = toReply, count=1)
    slmsg= str(tweets)
    lmsg=slmsg[60:180]
    
    #Creates a file text to save the last id and compare it to the new one.
    try:
        l=open('lmsg.txt','r')
        l.close()
        
    except:
        l=open('lmsg.txt','a+')
        l.write('IDs will be included here')
        l.close()
        
    with open('lmsg.txt', 'r') as lineas:
        for linea in lineas:
            if lmsg == linea:
                print('there is no new Tweets')
            elif lmsg != linea:
                print('New Tweet!')
                with open('lmsg.txt','w') as f:
                        f.write(lmsg)
                try:
                    for tweet in tweets:
                        api.update_status("@" + toReply + ' ' + message, in_reply_to_status_id = tweet.id)
                except:
                    break
while True:
    automsg()
    time.sleep(600) #Checks every 10 minutes if there is a new tweet
                            
