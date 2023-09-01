from service import Service


class Zvuk(Service):
    def send_sms(self):
        url = 'https://app.zvuk-b2b.com/api/v1/graphql/'

        payload = {
            'operationName': 'authCodeCreate',
            'variables': {
                'input': {
                    'phone': '+' + self.phone
                }
            },
            'query': 'mutation authCodeCreate($input: AuthorizationCodeCreateMutationInput!) {\n  authorizationCodeCreate(input: $input) {\n    ok\n    errors {\n      messages\n      __typename\n    }\n    codeData {\n      isActive\n      phone\n      created\n      __typename\n    }\n    __typename\n  }\n}\n'
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
