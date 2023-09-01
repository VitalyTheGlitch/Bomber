from service import Service


class Vkusnoitochka(Service):
    def send_sms(self):
        url = 'https://site-api.vkusnoitochka.ru/api/v1/user/login/phone'

        payload = {
            'g-recaptcha-response': '03AAYGu2TsWxYQs9zfDRidJPg0jAxIXc6ugRz6v8lN2uJAc0fN5W8LJ0zDqQ2OqwmEwl87_Jn-1aYI2sp3taZ71yUtt4Dq8SIuSxJ5pdRL5zjiTtqv5jG-OkJ_rYgwzAwpg-Sn5syDWfZ5uZf5j3T0RBbxr4MK8Y4nXlFYqwL3sXMoVsjBJ0j3UAX_IrM7_rGKz9043mgjb065A5hzquEUH5Re6zM6BJdouXnPQ1RuHyUtDpDY3FBVa4MT4wH7LuFjyDa7-Qjz0gvXwfdPrBnOxXV5oBXFujN8_n3C8hGB64rWpXIbFJoAMNU9bk6S-2euo0o0VUhUIZKh89f4hl-hTF39yj6m2FxGRBH1fw0tH5Wkb_bXZhhuxIz-3ApY2mIFE9Zp22EaT2LEP4ELb6N35F5-Dv-oeLN-vQ6Dp3Cju3FtkWm6VuIrKC1yFGb5SuJoXhuT-G4QiDJ4tUu4yY6cai4Jf_RSFoP4jLLO670YlfBvcQYsj02qOVcSimdHvfDoOddZW912JzKuQHAJscHRrTgM-inzxty32Ppe6V7Hd5svjQ76eyDzLNCsihv0iKkM7XglHDRaYGLN',
            'number': '+' + self.phone
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
