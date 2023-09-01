from service import Service


class MosMetro(Service):
    def send_sms(self):
        url = 'https://auth.mosmetro.ru/api/auth/login/sms'

        payload = {
            'login': self.phone,
            'returnUrl': ''
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
