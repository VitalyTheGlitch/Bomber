from service import Service


class FourLapy(Service):
    def send_sms(self):
        url = 'https://4lapy.ru/ajax/confirmation/phone/send-code'

        payload = {
            'form_type': 'form_registration_on_site',
            'phone': f'+{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}',
            'resend': False
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
