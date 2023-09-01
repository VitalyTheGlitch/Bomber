from service import Service


class Letu(Service):
    def send_sms(self):
        url = 'https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU'

        phone = f'+{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'

        payload = {
            'phoneNumber': phone
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
