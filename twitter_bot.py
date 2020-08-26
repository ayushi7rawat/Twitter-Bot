import tweepy
import time

print('HII, I am pymoonbot')
#Authenticate to Twitter
CONSUMER_KEY = 'your CONSUMER_KEY goes here'
CONSUMER_SECRET = 'your CONSUMER_SECRET goes here'
ACCESS_KEY = 'your ACCESS_KEY goes here'
ACCESS_SECRET = 'your ACCESS_SECRET goes here'

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user= api.me()
search = '#python3'
num_tweet = 350

#fetching tweets
for tweet in tweepy.Cursor(api.search, search).items(num_tweet):
	try:
		print('Tweet Liked')
		tweet.favorite()
		
		print('Retweet done')
		tweet.retweet()
		time.sleep(10)
		
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

