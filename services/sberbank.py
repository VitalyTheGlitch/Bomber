from service import Service


class SberBank(Service):
    def send_sms(self):
        url = 'https://online.sberbank.ru/CSAFront/uapi/v2/authenticate'

        payload = {
            'identifier': {
                'type': 'phone',
                'data': {
                'value': self.phone
                }
            },
            'authenticator': {
                'type': 'sms_otp',
                'data': {}
            },
            'channel': {
                'type':'web',
                'user_type':
                'private',
                'data': {
                    'rsa_data': {
                        'dom_elements': '',
                        'htmlinjection': '',
                        'manvsmachinedetection': '',
                        'js_events': '',
                        'deviceprint': 'version=1.7.3&pm_br=Chrome&pm_brmjv=115&iframed=0&intip=&pm_expt=&pm_fpacn=Mozilla&pm_fpan=Netscape&pm_fpasw=cwtouks15fknohls9eu268e2bnl5cwto|xcom6lswbaijrvaf|dozzrdoufu26gdjml5kxbair8hi47lso|hqqnbsexq0a0dgy&pm_fpco=1&pm_fpjv=0&pm_fpln=lang=ru-RU|syslang=|userlang=&pm_fpol=true&pm_fposp=&pm_fpsaw=1087&pm_fpsbd=&pm_fpsc=24|1087|977|977&pm_fpsdx=&pm_fpsdy=&pm_fpslx=&pm_fpsly=&pm_fpspd=24&pm_fpsui=&pm_fpsw=&pm_fptz=4&pm_fpua=mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36|5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36|Win32&pm_fpup=&pm_inpt=&pm_os=Windows&adsblock=0=false|1=false|2=false|3=false|4=false&audio=baseLatency=0.01|outputLatency=0|sampleRate=48000|state=suspended|maxChannelCount=2|numberOfInputs=1|numberOfOutputs=1|channelCount=2|channelCountMode=max|channelInterpretation=speakers|fftSize=2048|frequencyBinCount=1024|minDecibels=-100|maxDecibels=-30|smoothingTimeConstant=0.8&pm_fpsfse=true&webgl=ver=webgl2|vendor=Google Inc. (NVIDIA)|render=ANGLE (NVIDIA, NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0, D3D11)'},'oidc':{'scope':'address_reg birthdate email mobile name openid verified','response_type':'code','redirect_uri':'https://profile.sber.ru','state':'ad99ff12-7f5d-4799-b5bc-740f187dd909','nonce':'aadd333f-5bce-4b7b-8b2e-f1365a1fe79b','client_id':'2679efe6-f358-4378-b328-45dfcc4a006a','referer_uri':'https://profile.sber.ru/'
                    },
                    'browser': 'Chrome',
                    'os': 'Windows 10'
                }
            }
        } 

        r = self.session.post(url, json=payload, verify=False, timeout=5)

        return r.status_code, r.text
