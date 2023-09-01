from service import Service


class Cdek(Service):
    def send_sms(self):
        url = 'https://www.cdek.ru/api-site/auth/send-code'

        payload = {
            'locale': 'ru',
            'websiteId': 'ru',
            'phone': '+' + self.phone,
            'token': None
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
