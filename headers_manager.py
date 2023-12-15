from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent

def format_headers(headers):
    return {header['name'].lower(): header['value'] for header in headers if not header['name'].startswith(':') and header['name'].lower() != 'user-agent'}


def intercept(request):
    global headers

    request_headers = format_headers(request.headers_array())

    if 'akbars' in request.url and 'cookie' in request_headers:
        headers['Akbars'] = request_headers

    elif 'elementaree' in request.url and 'authorization' in request_headers:
        headers['Elementaree'] = request_headers

    elif 'leomax' in request.url and 'authorization' in request_headers:
        headers['LeoMax'] = request_headers

    elif 'megafon' in request.url and 'cookie' in request_headers:
        headers['Megafon'] = request_headers

    elif 'ostin' in request.url and 'cookie' in request_headers:
        headers['Ostin'] = request_headers

    elif '3332222' in request.url and 'x-csrf-token' in request_headers:
        headers['PizzaMafia'] = request_headers

    elif 'vprok' in request.url and 'x-xsrf-token' in request_headers:
        headers['Vprok'] = request_headers


def update_headers():
    global headers

    user_agent = UserAgent(verify_ssl=False)

    headers = {}

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()

        context = browser.new_context(user_agent=user_agent.random)    

        page = context.new_page()

        page.on('requestfinished', intercept)

        try:
            page.goto('https://akbars.ru', wait_until='networkidle', timeout=10000)
        except:
            pass

        try:
            page.goto('https://elementaree.ru/auth/', wait_until='networkidle', timeout=10000)
        except:
            pass

        headers['SberBank'] = {
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://online.sberbank.ru/'
        }

        try:
            page.goto('https://leomax.ru/', wait_until='networkidle', timeout=10000)
        except:
            pass

        try:
            page.goto('https://megafon.tv', wait_until='networkidle', timeout=10000)
        except:
            pass

        try:
            page.goto('https://ostin.com', wait_until='networkidle', timeout=10000)
        except:
            pass

        try:
            page.goto('https://3332222.ru', wait_until='networkidle', timeout=10000)
        except:
            pass

        headers['Raiffeisen'] = {
            'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/'
        }

        try:
            page.goto('https://vprok.ru', wait_until='networkidle', timeout=10000)
        except:
            pass

        page.remove_listener('requestfinished', intercept)

        context.close()


def get_headers(service):
    global headers

    return headers.get(service, {})


update_headers()

print(get_headers('LeoMax'))
print()
print(get_headers('Megafon'))
print()
print(get_headers('Ostin'))
