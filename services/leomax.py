from service import Service


class LeoMax(Service):
    def send_sms(self):
        url = 'https://ap.leomax.ru/siteapi/auth/authcode'

        payload = {
            'phone': '+' + self.phone
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
