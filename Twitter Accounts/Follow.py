import time
import os
import twitter
f = open('done.txt','w')
screen_names = [line.rstrip('\n') for line in open('twitter.account')]
ck = os.getenv("TWITTER_CONSUMER_TOKEN")
cs = os.getenv("TWITTER_CONSUMER_TOKEN_SECRET")
at = os.getenv("TWITTER_ACCESS_TOKEN")
ats = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
t = twitter.Api(consumer_key=ck, consumer_secret=cs, access_token_key=at, access_token_secret=ats, sleep_on_rate_limit=True)
for a_screen_name in screen_names:
    try:
        x = str(a_screen_name)
        print(x)
        t.CreateFriendship(screen_name=x, follow=True, retweets=True)
        f.writelines(a_screen_name)
    except twitter.error.TwitterError as e:
        if e.message[0]['code'] == 108:
            pass
        else:
            print(e.message)
    time.sleep(65)
