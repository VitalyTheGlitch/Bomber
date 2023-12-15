import requests
import os
import sys
import random
import secrets
import string
from datetime import datetime
from fake_useragent import UsrAgent
from urllib3.exceptions import InsecureRequestWarning

class Service:
    user_agent = UserAgent(verify_ssl=False)

    def __init__(self, phone, headers={}, proxy=''):
        self.phone = phone
        self.session = requests.Session()
        self.session.headers = headers
        self.session.headers['User-Agent'] = self.generate_user_agent()

        if os.path.isfile('debug'):
            self.session_get = self.session.get
            self.session_post = self.session.post
            self.session.get = self.get
            self.session.post = self.post

        if proxy:
            self.session.proxies.update({
                'https': proxy
            })

        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    @staticmethod
    def _log_request(name, message):
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {name}: {message}')

    def get(self, *args, **kwargs):
        request = self.session_get(*args, **kwargs)

        logging_text = request.text

        if len(logging_text) > 500:
            if '<!doctype html>' in logging_text.lower():
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is HTML'

            else:
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is not HTML'

        self._log_request(type(self).__name__, logging_text.replace('\n', ''))

        return request

    def post(self, *args, **kwargs):
        request = self.session_post(*args, **kwargs)

        logging_text = request.text

        if len(logging_text) > 500:
            if '<!doctype html>' in logging_text.lower():
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is HTML'

            else:
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is not HTML'

        self._log_request(type(self).__name__, logging_text.replace('\n', ''))

        return request

    @staticmethod
    def generate_user_agent():
        return Service.user_agent.random

    @staticmethod
    def generate_password():
        symbols = [secrets.choice(string.ascii_uppercase) for i in range(5)] + \
                  [secrets.choice(string.ascii_lowercase) for i in range(5)] + \
                  [secrets.choice(string.digits) for i in range(5)] + \
                  [secrets.choice('<>(){}!?.,:;+-=~_\\"^*@#$%|') for i in range(5)]

        password = ''.join(random.sample(symbols, len(symbols)))

        return password
