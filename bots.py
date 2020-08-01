import logging

from jisho import Client
import tweepy

logging.basicConfig(level=logging.DEBUG)


class TwitterBot:
    def __init__(self, config):
        auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
        auth.set_access_token(config['access_token'], config['access_token_secret'])
        # self._api = tweepy.API(auth)
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

    def run(self):
        logging.info('Testing')
        results = self.translate('house')

        for result in results:
            for lang, info in result.items():
                print(f'{lang}: {info}')

        logging.debug(self._api.me().name)
        logging.info('Tweeting...')

        # TODO
        # self._api.update_status(status='Updating using OAuth authentication via Tweepy!')
