import json
import time
from pathlib import Path
import re

from selenium.common.exceptions import InvalidCookieDomainException

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from urllib import parse


class SelDriver:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        self.m_html = None
        self.options = Options()

        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('prefs',
                                             {
                                                 'profile.managed_default_content_settings.images': 2,
                                                 # 'profile.managed_default_content_settings.mixed_script': 2,
                                                 # 'profile.managed_default_content_settings.media_stream': 2,
                                                 # 'profile.managed_default_content_settings.stylesheets': 2
                                             })

        # self.options.add_argument("--headless")
        self.options.add_argument(f"--user-agent={self.user_agent}")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--profiling-flush=n')
        self.options.add_argument('--enable-aggressive-domstorage-flushing')
        self.options.add_argument("--disable-notifications")
        self.options.page_load_strategy = 'eager'

        # self.service = Service(executable_path="../../Chrome/chromedriver.exe")
        # self.options.binary_location = "../../Chrome/chrome-win64/chrome.exe"

        self.driver = webdriver.Chrome(options=self.options)

    def getProductList(self, account, result):
        with (open("cities.txt", "r", encoding='utf-8') as cities):
            for city in cities:
                while True:
                    try:
                        time.sleep(2)
                        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
                        geo = self.driver.find_element(By.ID, "hyperlocation-unified-dialog-anchor")
                        geo.click()
                        time.sleep(2)
                        button = self.driver.find_element(By.XPATH, f"//div[@data-auto='{city.split('/')[1][0:-1]}']")
                        button.click()
                        time.sleep(2)
                        break
                    except:
                        print(account)

                with (open("products.txt", "r", encoding='utf-8') as products):
                    for prod in products:
                        if not prod.split()[0] in result:
                            result[prod.split()[0]] = {}

                        self.driver.get(prod.split()[1])

                        for i in range(10):
                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                            time.sleep(0.5)  # время для загрузки страницы

                        items = BeautifulSoup(self.driver.page_source, 'lxml').find_all("div", attrs={
                            "data-apiary-widget-name": "@light/Organic"})

                        for i in items:
                            title = i.find("div", attrs={"data-baobab-name": "title"})
                            if title:

                                if "без" in str(i.find("div", attrs={"data-baobab-name": "price"})):
                                    price = i.find(attrs={"data-auto": "snippet-price-old"}).find_all()[0]
                                else:
                                    price = i.find(attrs={"data-auto": "snippet-price-current"}).find_all()[0]

                                url = title.find("a").get("href")
                                sku = str(parse.parse_qs(parse.urlparse(url).query)["sku"][0])

                                if title.text == "":
                                    title = (re.split("[<>]", str(title.find("span")))[2])
                                else:
                                    title = title.text

                                if price.text == "":
                                    price = (re.split("[<>]", str(price))[2])
                                else:
                                    price = price.text

                                if sku in result[prod.split()[0]]:
                                    result[prod.split()[0]][sku].append(
                                        [title, int(price.replace("\u2009", "")), city.split("/")[0], account, url])
                                else:
                                    result[prod.split()[0]][sku] = [
                                        [title, int(price.replace("\u2009", "")), city.split("/")[0], account, url]]
        return result

    def load_cookies(self, cookies_path):
        cookies = json.load(open(cookies_path, "rb"))
        self.driver.get('https://market.yandex.ru/')
        for cookie in cookies:
            if 'sameSite' in cookie:
                cookie['sameSite'] = 'Lax'
            try:
                self.driver.add_cookie(cookie)
            except InvalidCookieDomainException:
                print("loggining")

    def scraper_quit(self):
        self.driver.close()
        self.driver.quit()

def main_pars():
    result = {}
    p = Path("cookies")
    for cookies in p.rglob("*"):
        driver = SelDriver()

        driver.load_cookies(cookies)
        driver.driver.get('https://market.yandex.ru/')
        new_result = driver.getProductList(re.split('[. ]', str(cookies))[2], result)
        result = new_result
        driver.scraper_quit()

    with open("result.json", "w") as file:
        json.dump(result, file)

    return result

if __name__ == "__main__":
    main_pars()


