import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
from urllib.parse import urljoin

def get_absolute_url(relative_url):
    base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    return urllib.parse.urljoin(base_url, relative_url)

def save_image(image_url, image_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join("fetched_images", image_name), 'wb') as f:
            f.write(response.content)
    else:
        print(f"Erreur lors du téléchargement de l'image {image_url}. Code d'état : {response.status_code}")

def save_book_info(book_info, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(book_info)
        file.write('\n\n')

def get_book_info(book_url):
    response = requests.get(book_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_page_url = book_url
        upc = soup.find('th', text='UPC').find_next('td').text
        title = soup.find('h1').text
        price_including_tax = soup.find('th', text='Price (incl. tax)').find_next('td').text
        price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next('td').text
        number_available = soup.find('th', text='Availability').find_next('td').text
        product_description = soup.find('meta', {'name': 'description'})['content']
        category = soup.select('ul.breadcrumb li')[-2].text.strip()
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        image_url = urljoin(book_url, soup.find('img')['src'])
        image_name = f"{upc}.jpg"

        save_image(image_url, image_name)

        book_info = (
            f"Product Page URL: {product_page_url}\n"
            f"UPC: {upc}\n"
            f"Title: {title}\n"
            f"Price (Including Tax): {price_including_tax}\n"
            f"Price (Excluding Tax): {price_excluding_tax}\n"
            f"Number Available: {number_available}\n"
            f"Product Description: {product_description}\n"
            f"Category: {category}\n"
            f"Review Rating: {review_rating}\n"
            f"Image URL: {image_url}\n"
            f"Image saved as: {image_name}\n"
        )

        save_book_info(book_info, os.path.join("generated_datas", "book_info.txt"))

        print("Informations du livre sauvegardées dans generated_datas/book_info.txt\n")
    else:
        print(f"Erreur lors de la requête pour {book_url}. Code d'état : {response.status_code}")

def scrape_category_pages(base_url):
    current_page = 1
    while True:
        url = f"{base_url}/page-{current_page}.html"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.select('h3 a')

            if not books:
                break

            book_urls = [get_absolute_url(book['href']) for book in books]

            for book_url in book_urls:
                get_book_info(book_url)

            current_page += 1
        else:
            print(f"Plus de livre à scrapper")
            if response.status_code == 404:
                break  # Arrêtez la boucle si la page demandée n'existe pas

base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3'
# Créez le dossier "generated_datas" s'il n'existe pas déjà
os.makedirs("generated_datas", exist_ok=True)
scrape_category_pages(base_url)
