from twython import Twython, TwythonError

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv
