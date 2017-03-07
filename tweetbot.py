from twython import Twython, TwythonError

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


for number in [1,2,3]:
    try:
        twitter.update_status(status='% times % = %' % [number, number, number*number])
    except TwythonError as e:
        print e

# read from csv
