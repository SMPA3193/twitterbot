from twython import Twython, TwythonError

APP_KEY = 'uqdFqqqnBq4ruOaGR1e2P2M9D'
APP_SECRET = 'LpIvtuF9Gjb3EwMObQ22VOUVgj1HiZi7n5caVeZ3wJ98hDSqOQ'
OAUTH_TOKEN = '722556363721818113-jGlE6zQLKMAn4DJqtz6MOyC7CCXODNB'
OAUTH_TOKEN_SECRET = 'vAnhXdWepDcB2XHQYjzViarCMbXFM0pqPSPqfQqgk8Kpq'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e

# read from csv
