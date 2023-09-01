from service import Service


class Infoer(Service):
    def send_sms(self):
        url = 'https://info-api.er.ru/api/auth/authenticate'

        payload = {
            'phone': self.phone[1:]
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
