from service import Service


class Megafon(Service):
    def send_sms(self):
        url = 'https://bmp.megafon.tv/api/v10/auth/register/msisdn'

        payload = {
            'msisdn': '+' + self.phone,
            'password': self.generate_password()
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
