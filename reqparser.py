import requests

from bs4 import BeautifulSoup

cookies = {
    'i': 'dz71oIcHVGxtjfQirF95G+2Bi60R3h7pJojwBhQ8nNqpMPrzZjpNMjHGDXjKZprg3dk9MfVkLzeWi5q9LdUOFI9Psvc=',
    'yandexuid': '1765291121728786184',
    'yashr': '3249538591728786184',
    'receive-cookie-deprecation': '1',
    'visits': '1728786185-1728786185-1728786185',
    'cmp-merge': 'true',
    'reviews-merge': 'true',
    'skid': '1139571571728786185',
    'oq_shown_onboardings': '%5B%5D',
    'oq_last_shown_date': '1728786185621',
    'muid': '1152921512451365187%3A4NeHeaNYTl%2BWTqUJPgrc%2FrZohW5UXFjk',
    'is_gdpr': '0',
    'yuidss': '1765291121728786184',
    'ymex': '2044146186.yrts.1728786186',
    '_ym_uid': '1728786185630262170',
    '_ym_d': '1728786186',
    '_ym_isad': '1',
    'ygu': '0',
    'nec': '0',
    'yandexmarket': '48%2CRUR%2C1%2C%2C%2C%2C2%2C0%2C0%2C38%2C0%2C0%2C12%2C0%2C0',
    'yandex_gid': '38',
    'is_gdpr_b': 'CP/jIhCtmAIoAg==',
    'user_unchecked_cart_item_ids': '%5B%5D',
    'server_request_id_market:index': '1728838157252%2F710c892d1a496f2814b83c805e240600%2F1%2F1',
    'rcrr': 'true',
    'ugcp': '1',
    'suppress_order_notifications': '1',
    'gdpr': '0',
    'global_delivery_point_skeleton': '{%22deliveryType%22:%22PICKUP%22%2C%22outletType%22:%22pickup%22%2C%22regionName%22:%22%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4%22%2C%22addressLineWidth%22:100.03125}',
    '_yasc': 'Egf9t3n2WuTwRRXSmF1IkyeglAp698sSmFb3onoa35T3UZi0sUXnGun8Elx1Ak02jSUT5sx2mcp1rOHEoQ==',
    'parent_reqid_seq': '1728838194528%2F924bd909a7e9e8ecfc8075825e240600%2F1%2F1%2C1728838212392%2F266bc732b2e5d973781586835e240600%2F1%2F1%2C1728838288435%2F70a8e8d7b3714890c7680e885e240600%2F1%2F1%2C1728838295442%2F8e240fa72fbb9df8705579885e240600%2F1%2F1%2C1728838312324%2F103a0164617e41d632ed7a895e240600%2F1%2F1',
    'bh': 'EkAiR29vZ2xlIENocm9tZSI7dj0iMTI5IiwgIk5vdD1BP0JyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMjkiKgI/MDoJIldpbmRvd3MiYKn1r7gGah7cyuH/CJLYobEDn8/h6gP7+vDnDev//fYPtZbNhwg=',
}

headers = {
    'Host': 'market.yandex.ru',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
}

params = {
    'suggest_text': 'колонка алиса',
    'resale_goods': 'resale_new',
}

response = requests.get(
    'https://market.yandex.ru/catalog--smartfony/16814639/list?hid=91491&glfilter=16816262:16816264&onstock=1',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)

m_html = BeautifulSoup(response.text, 'lxml')
print(m_html)

# .find("div", attrs={"data-auto": "SerpList"})