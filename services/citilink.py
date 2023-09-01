from service import Service


class Citilink(Service):
    def send_sms(self):
        url = f'https://www.citilink.ru/registration/confirm/phone/+{self.phone}/'

        r = self.session.post(url, timeout=5)

        return r.status_code, r.text
