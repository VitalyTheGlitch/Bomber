from service import Service


class WineLab(Service):
    def send_sms(self):
        url = f'https://www.winelab.ru/confirmation/sendByPhone?number={self.phone[1:4]} {self.phone[4:7]} {self.phone[7:9]} {self.phone[9:11]}'

        r = self.session.get(url, timeout=5)

        return r.status_code, r.text
