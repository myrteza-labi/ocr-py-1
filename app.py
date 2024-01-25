import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_absolute_url(relative_url):
    base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    return urllib.parse.urljoin(base_url, relative_url)

def get_book_info(book_url):
    response = requests.get(book_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupérer les informations nécessaires
        product_page_url = book_url
        upc = soup.find('th', text='UPC').find_next('td').text
        title = soup.find('h1').text
        price_including_tax = soup.find('th', text='Price (incl. tax)').find_next('td').text
        price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next('td').text
        number_available = soup.find('th', text='Availability').find_next('td').text
        product_description = soup.find('meta', {'name': 'description'})['content']
        category = soup.select('ul.breadcrumb li')[-2].text.strip()
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        image_url = soup.find('img')['src']

        # Afficher les informations
        print("Product Page URL:", product_page_url)
        print("UPC:", upc)
        print("Title:", title)
        print("Price (Including Tax):", price_including_tax)
        print("Price (Excluding Tax):", price_excluding_tax)
        print("Number Available:", number_available)
        print("Product Description:", product_description)
        print("Category:", category)
        print("Review Rating:", review_rating)
        print("Image URL:", image_url)
        print("\n")
    else:
        print(f"Erreur lors de la requête pour {book_url}. Code d'état : {response.status_code}")

url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    book_urls = []
    books = soup.select('h3 a')

    for book in books:
        relative_url = book['href']
        absolute_url = get_absolute_url(relative_url)
        book_urls.append(absolute_url)

    for book_url in book_urls:
        get_book_info(book_url)
else:
    print(f"Erreur lors de la requête. Code d'état : {response.status_code}")
