from service import Service


class Vprok(Service):
    def send_sms(self):
        url = 'https://www.vprok.ru/as_send_pin'

        payload = {
            'phone': self.phone
        }

        r = self.session.post(url, payload, timeout=5)

        return r.status_code, r.text
