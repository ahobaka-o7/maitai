import logging
import random

from jisho import Client
import tweepy

logging.basicConfig(level=logging.DEBUG)


class TwitterBot:
    def __init__(self, config):
        auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
        auth.set_access_token(config['access_token'], config['access_token_secret'])
        self._api = tweepy.API(auth)
        self._jisho = Client()

    def translate(self, word):
        resp = self._jisho.search(word)
        results = []
        for item in resp['data']:
            english = []
            for sense in item['senses']:
                english += sense['english_definitions']

            japanese = []
            for jp in item['japanese']:
                try:
                    japanese += jp['word']
                except KeyError:
                    # Katakana version?
                    logging.error(jp)

            result = {
                'en': english,
                'jp': japanese,
            }

            results.append(result)

        return results

    def get_random_japanese(self):
        # TODO
        words = ['house']
        choice = random.choice(words)
        return choice

    def get_first_tweet_id(self):
        # TODO
        return 0

    def run(self):
        logging.info('Testing')

        japanese_word = self.get_random_japanese()
        results = self.translate(japanese_word)

        for result in results:
            for lang, info in result.items():
                print(f'{lang}: {info}')

        logging.debug(self._api.me().name)
        logging.info('Tweeting...')

        status1 = ''

        # First tweet
        self._api.update_status(status=status1)

        # Second tweet
        # TODO
        status2 = ''
        in_reply_to_status_id = self.get_first_tweet_id()
        self._api.update_status(status2, in_reply_to_status_id=in_reply_to_status_id)
