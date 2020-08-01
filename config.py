from os import environ as env


class AppConfig:
    def __init__(self):
        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located
        # under "Your access token")
        self.twitter = {
            'consumer_key': env['TWITTER_CONSUMER_KEY'],
            'consumer_secret': env['TWITTER_CONSUMER_SECRET'],
            'access_token': env['TWITTER_ACCESS_TOKEN'],
            'access_token_secret': env['TWITTER_ACCESS_TOKEN_SECRET']
        }
