from service import Service


class Gosuslugi(Service):
    def send_sms(self):
        url = 'https://online.sberbank.ru/CSAFront/api/esia/restore/identificate'

        payload = {
            'phoneNumber': self.phone,
            'deviceprint': 'version=1.7.3&pm_br=Chrome&pm_brmjv=115&iframed=0&intip=&pm_expt=&pm_fpacn=Mozilla&pm_fpan=Netscape&pm_fpasw=zqiml5cwtwbir899|wgvf2bntwyzrdwlfh36gls9e2j47dt1d|yvf2j4fco7gdbny|wyzzcbfxyzrvxyuxg368e2j47dt9mb05&pm_fpco=1&pm_fpjv=0&pm_fpln=lang=ru-RU|syslang=|userlang=&pm_fpol=true&pm_fposp=&pm_fpsaw=1088&pm_fpsbd=&pm_fpsc=24|1088|980|980&pm_fpsdx=&pm_fpsdy=&pm_fpslx=&pm_fpsly=&pm_fpspd=24&pm_fpsui=&pm_fpsw=&pm_fptz=4&pm_fpua=mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/115.0.0.0 safari/537.36|5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36|Win32&pm_fpup=&pm_inpt=&pm_os=Windows&adsblock=0=false|1=false|2=false|3=false|4=false&audio=baseLatency=0.01|outputLatency=0|sampleRate=48000|state=running|maxChannelCount=2|numberOfInputs=1|numberOfOutputs=1|channelCount=2|channelCountMode=max|channelInterpretation=speakers|fftSize=2048|frequencyBinCount=1024|minDecibels=-100|maxDecibels=-30|smoothingTimeConstant=0.8&pm_fpsfse=true&webgl=ver=webgl2|vendor=Google Inc. (NVIDIA)|render=ANGLE (NVIDIA, NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0, D3D11)'
        }

        r = self.session.post(url, json=payload, timeout=5)

        return r.status_code, r.text
