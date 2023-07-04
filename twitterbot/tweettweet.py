import tweepy

auth = tweepy.OAuthHandler('PvlQOhwGZCP0iU8LzeYQ12g2E', 'pgkOgT5kmH94W9oKCZHmDfa9zlEjtAGCAGPij8RKdSCszsZ5kq')
auth.set_access_token('1507298470020927492-KA5n8R8nWTkIWmuvU120o7yycx8Ngy', 'RQCYov5oZTHPyQCV7xBRs9VXYd09EM5yU11G6t5BpzWxE')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


#  generous Bot (Follows each follower back)
#  for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()


#  Narcissist Bot (likes tweets that contain my username (which are 0 of course) )
search_string = 'ahemyu1'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

