from service import Service


class Raiffeisen(Service):
    def send_sms(self):
        url = 'https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms'

        payload = {
            'number': self.phone
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
