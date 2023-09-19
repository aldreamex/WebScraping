import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# driver = uc.Chrome()
# driver.get('https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1')

class AvitoScrap:
    def __init__(self, url: str, items: list, count: int=100):
        self.url = url
        self.items = items
        self.count = count
        self.data = []

    def __set_up(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = uc.Chrome(options=options)

    def __get_url(self):
        self.driver.get(self.url)

    def __paginator(self):
        while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']") and self.count > 0:
            self.__scrap_page()
            self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
            self.count += 1

    def __scrap_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            descriptions = title.find_element(By.CSS_SELECTOR, "[data-marker='item-specific-params']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
            data = {
                'name': name,
                'descriptions': descriptions,
                'url': url,
                'price': price,
            }

            if any([item in descriptions for item in self.items]):
                self.data.append(data)

            # print(name, descriptions, url, price)
        self.__save_data()


    def __save_data(self):

        sorted_data = sorted(self.data, key=lambda x: float(x['price']))

        with open("items.json", 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, indent=4)



    def scraping(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()

if __name__=="__main__":
    AvitoScrap(url='https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&s=104',
               count=1,
               items=['без залога']
               ).scraping()

