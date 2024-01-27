import csv
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
from urllib.parse import urljoin
import re

def clean_title_for_filename(title):
    cleaned_title = re.sub(r'[^a-zA-Z0-9 ]', '', title)
    cleaned_title = cleaned_title.replace(' ', '_')
    return cleaned_title

def get_image_name(title):
    cleaned_title = clean_title_for_filename(title)
    return f"{cleaned_title}.jpg"

def get_absolute_url(relative_url):
    base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    return urllib.parse.urljoin(base_url, relative_url)

def save_image(image_url, image_name):
    file_path = os.path.join("fetched_images", image_name)

    if os.path.exists(file_path):
        os.remove(file_path)  # Supprimer le fichier existant

    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Erreur lors du téléchargement de l'image {image_url}. Code d'état : {response.status_code}")

def save_book_info_csv(book_info, file_path):
    fieldnames = [
        'product_page_url', 'universal_product_code', 'title',
        'price_including_tax', 'price_excluding_tax', 'number_available',
        'product_description', 'category', 'review_rating', 'image_url'
    ]

    with open(file_path, 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Écrivez les en-têtes une seule fois
        if os.stat(file_path).st_size == 0:
            writer.writeheader()

        writer.writerow(book_info)

def get_book_info_csv(book_url):
    response = requests.get(book_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').text
        upc = soup.find('th', text='UPC').find_next('td').text
        price_including_tax = soup.find('th', text='Price (incl. tax)').find_next('td').text
        price_excluding_tax = soup.find('th', text='Price (excl. tax)').find_next('td').text
        number_available = soup.find('th', text='Availability').find_next('td').text
        product_description = soup.find('meta', {'name': 'description'})['content']
        category = soup.select('ul.breadcrumb li')[-2].text.strip()
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        image_url = urljoin(book_url, soup.find('img')['src'])
        image_name = get_image_name(title)

        save_image(image_url, image_name)

        book_info = {
            'product_page_url': book_url,
            'universal_product_code': upc,
            'title': title,
            'price_including_tax': price_including_tax,
            'price_excluding_tax': price_excluding_tax,
            'number_available': number_available,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url
        }

        save_book_info_csv(book_info, os.path.join("CSVs", "book_info.csv"))

        print("Informations du livre sauvegardées dans CSVs/book_info.csv\n")
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
                get_book_info_csv(book_url)

            current_page += 1
        else:
            print(f"Plus de livre à scrapper")
            if response.status_code == 404:
                break  # Arrêtez la boucle si la page demandée n'existe pas

# Créez le dossier "CSVs" s'il n'existe pas déjà
os.makedirs("CSVs", exist_ok=True)
os.makedirs("fetched_images", exist_ok=True)

base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3'
scrape_category_pages(base_url)
