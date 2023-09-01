from service import Service


class ICQ(Service):
    def send_sms(self):
        url = 'https://u.icq.net/api/v89/rapi/auth/sendCode'

        payload = {
            'reqId': '85231-1668029727',
            'params': {
                'phone': self.phone,
                'language': 'en-US',
                'route': 'sms',
                'devId': 'ic1rtwz1s1Hj1O0r',
                'application': 'icq'
            }
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
