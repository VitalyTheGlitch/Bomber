from service import Service


class Dixy(Service):
    def send_sms(self):
        url = 'https://dostavka.dixy.ru/ajax/mp-auth-test.php'

        payload = {
            'phone': '+' + self.phone,
            'licenses_popup': 'Y',
            'licenses_popup3': 'Y',
            'licenses_popup1': 'Y'
        }

        r = self.session.post(url, payload, timeout=5)

        return r.status_code, r.text
