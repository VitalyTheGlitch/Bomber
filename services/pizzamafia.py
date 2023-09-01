from service import Service


class PizzaMafia(Service):
    def send_sms(self):
        url = 'https://3332222.ru/phone/validate'

        payload = {
            'phone': f'+{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]} '
        }

        r = self.session.post(url, json=payload, verify=False, timeout=5)

        return r.status_code, r.text
