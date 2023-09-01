from service import Service


class KnopkaDengi(Service):
    def send_sms(self):
        url = f'https://knopkadengi.ru/api/registration/send/code?mobilePhone={self.phone[1:]}'

        r = self.session.post(url, timeout=5)

        return r.status_code, r.text
