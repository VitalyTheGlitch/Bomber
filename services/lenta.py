from service import Service


class Lenta(Service):
    def send_sms(self):
        url = 'https://lenta.com/api/v1/authentication/loginotp'

        payload = {
            'phoneNumber': self.phone
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
