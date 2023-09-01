from service import Service


class GPBInvest(Service):
    def send_sms(self):
        url = 'https://idp.gazprombank.investments/auth/realms/service/protocol/openid-connect/token'

        payload = {
            'client_id': 'web',
            'grant_type': 'password',
            'phone_number': '+' + self.phone
        }

        r = self.session.post(url, payload, timeout=5)

        return r.status_code, r.text
