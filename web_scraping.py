import requests
from bs4 import BeautifulSoup

url = "https://www.shopclues.com/search?q=Smartphone"
res = requests.get(url)
html_data = res.content
parsed_data = BeautifulSoup(html_data, "html.parser")
print(parsed_data.prettify())

titles = parsed_data.find_all('h2')

for title in titles:
    print(title)

new_prices = parsed_data.find_all('span', class_='p_price')

for new_price in new_prices:
    print(new_price)


old_prices = parsed_data.find_all('span',class_='old_prices')

for old_price in old_prices:
    print(old_price)

product_discounts = parsed_data.find_all('span',class_='prd_discount')

for product_discount in product_discounts:
    print(product_discount)

urls = parsed_data.find_all('a')


for url in urls:
    if 'href':
        print(url)


img_urls = parsed_data.find_all('div', class_='img_section')

for img_url in img_urls:
    if 'src':
        print(img_url)
