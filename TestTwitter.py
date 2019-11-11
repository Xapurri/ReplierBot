# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:49:32 2019

@author: Xavi
"""

import tweepy, time
#Access
consumer_key = '5aJQ9Mnm0pr1WBSBsmf9hTvn8'
consumer_secret = 'ARSR1prmtC5tIeLnrTGj63DbVf1uchtLvBb7hT63yEtWVPkkms'
access_token = '1116702622722002945-exohb0fNz9MnySjXkKAAoxGotoVaSq'
access_token_secret = 'lTcr0jxtQPlQWgqwds9oKa1wI55KziuAWMRIZeun3t5xN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''message= 'Hola'
api.update_status(message)'''
def automsg():
    #Sending a reply
    message= 'Que te calles, que eres tontísimo'
    toReply = "NoelleVanyi" 
    api = tweepy.API(auth)
    
    
    
    tweets = api.user_timeline(screen_name = toReply, count=1)
    slmsg= str(tweets)
    lmsg=slmsg[60:180]

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
                print('No hay nuevos tweets')
            elif lmsg != linea:
                print('¡Nuevo tweet!')
                with open('lmsg.txt','w') as f:
                        f.write(lmsg)
                try:
                    for tweet in tweets:
                        api.update_status("@" + toReply + ' ' + message, in_reply_to_status_id = tweet.id)
                except:
                    break
while True:
    automsg()
    time.sleep(600)
                            