import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from web_scraping.models import AvitoItem, FormData

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
        while self.count > 0:
            self.__scrap_page()
            next_button = self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']")
            if next_button.is_displayed():
                next_button.click()
                self.count -= 1
            else:
                break

    def __scrap_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            try:
                name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
                descriptions = title.find_element(By.CSS_SELECTOR, "[data-marker='item-specific-params']").text
                owner_descriptions = title.find_element(By.CSS_SELECTOR, "[class*='iva-item-descriptionStep']").text
                combined_description = f"{descriptions}\n{owner_descriptions}"
                url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
                price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
                created_at = title.find_element(By.CSS_SELECTOR, "[data-marker='item-date']").text
                data = {
                    'name': name,
                    'descriptions': combined_description,
                    'url': url,
                    'price': price,
                    'created_at': created_at,
                }

                description_words = combined_description.split()


                if all(item.lower() in ' '.join(description_words).lower() for item in self.items):

                    data = {
                        'name': name,
                        'descriptions': combined_description,
                        'url': url,
                        'price': price,
                        'created_at': created_at,
                    }
                    self.data.append(data)

            except Exception as e:
                print(f"Произошла ошибка: {str(e)}")

        sorted_data = sorted(self.data, key=lambda x: float(x['price']))

        for data in sorted_data:

            scraper_item = AvitoItem(name=data['name'],
                                   descriptions=data['descriptions'],
                                   url=data['url'],
                                   price=data['price'],
                                   created_at=data['created_at'],)
            scraper_item.save()


    # def __save_data(self):
    #
    #     sorted_data = sorted(self.data, key=lambda x: float(x['price']))
    #
    #     with open("items.json", 'w', encoding='utf-8') as f:
    #         json.dump(sorted_data, f, ensure_ascii=False, indent=4)
    def __clear_database(self):
        AvitoItem.objects.all().delete()
        FormData.objects.all().delete()

    def scraping(self):
        self.__set_up()
        self.__clear_database()
        self.__get_url()
        self.__paginator()
        # asas = FormData.objects.all()
        # print(asas)

# if __name__=="__main__":
#     AvitoScrap(url='https://www.avito.ru/bryansk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA',
#                count=1,
#                items=['Без комиссии']
#                ).scraping()

