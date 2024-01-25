import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    book_urls = []
    books = soup.select('h3 a')

    for book in books:
        product_page_url = book['href']
        book_urls.append('https://books.toscrape.com/catalogue' + product_page_url)
    for book_url in book_urls:
        print(book_url)
else:
    print(f"Erreur lors de la requête. Code d'état : {response.status_code}")
