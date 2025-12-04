import requests
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

def get_and_save_data():
    url = os.getenv('URL')

    response = requests.get(url)
    response.raise_for_status()

    json_data = response.json()

    books_list = json_data['data']

    books = pd.DataFrame(books_list)

    books.to_csv('data/books.csv', index=False)

