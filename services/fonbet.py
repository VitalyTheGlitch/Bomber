from service import Service


class FonBet(Service):
    def send_sms(self):
        url = 'https://clientsapi52w.bk6bba-resources.com/cps/superRegistration/createProcess'

        payload = {
            'fio': '',
            'password': self.generate_password(),
            'email': '',
            'emailAdvertAccepted': True,
            'phoneNumber': '+' + self.phone,
            'webReferrer': 'https://www.fon.bet/forecasts/?utm_referrer=https%3a%2f%2fsearch.brave.com%2f',
            'advertInfo': '',
            'platformInfo': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'promoId': '',
            'ecupis': True,
            'birthday': '2000-10-10',
            'sysId': 1,
            'lang': 'ru',
            'appVersion': '4.28.2',
            'deviceId': 'E91A637595B1C16FC27BDBB6BDF42A08'
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
