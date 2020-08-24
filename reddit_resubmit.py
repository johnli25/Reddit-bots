import praw
import datetime
from time import sleep
from random import randint
import time

# Put in script info, username, password, and user agent
# To access that info here, check here: https://www.reddit.com/prefs/apps 
reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = '',
                     password = '',
                     user_agent = '')

subreddit = reddit.subreddit("")

repost_submission = reddit.submission(url='')

reddit.validate_on_submit = True

#This program will rely on a post's selftext or body text.
#BUT strings can also be used instead. Ex: string = "Hello World"
recomment_submission = reddit.submission(url='')
selftext_comment = recomment_submission.selftext

while True: #run forever 24/7
    
#repost section
    title = ""
    selftext = repost_submission.selftext
    reddit.subreddit("").submit(title, selftext = selftext)

#recomment section
    for submission in reddit.subreddit("").hot(limit= 5): #any number limit you the programmer would like
        print("It works!")
        submission.reply(selftext_comment)
        
    time.sleep(10) #10 second timer (any time you, the programmer, would like)
