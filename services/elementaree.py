from service import Service


class Elementaree(Service):
    def send_sms(self):
        url = 'https://api-new.elementaree.ru/graphql'

        payload = {
            'operationName': 'phoneVerification',
            'variables': {
                'phone': self.phone
            },
            'query': 'mutation phoneVerification($phone: String!) {\n  phoneVerification(phone: $phone) {\n    success\n    interval\n    __typename\n  }\n}'
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
