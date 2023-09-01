from service import Service


class Ostin(Service):
    def send_sms(self):
        url = 'https://ostin.com/api/v2/front/request-code'

        payload = {
            'channel': 'SMS',
            'phone': '+' + self.phone,
            'recaptchaToken': ''
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
