import requests
from twython import Twython, TwythonError

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

r = requests.get("https://analytics.usa.gov/data/live/realtime.json")

try:
    twitter.update_status(status='Total Visitors Online: %s' % r.json()['data'][0]['active_visitors'])
except TwythonError as e:
    print e

