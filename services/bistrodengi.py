from service import Service


class BistroDengi(Service):
    def send_sms(self):
        url = 'https://zaim.bistrodengi.ru/api/loginLK'

        payload = {
            'fio': 'Иванов Александр Евгеньевич',
            'phone': f'+{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}',
            'birthdate': '11.02.2000',
            'sopdn': True,
            'sopdnAd': True,
            'url': 'https://zaim.bistrodengi.ru/',
            'referrer': 'https://zaim.bistrodengi.ru/?utm_source=bankiru&wmid=1&utm_content=102a727d1008a15f745e21630a8b6d'
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
