import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import TextLoader
from io import StringIO

def load_constitution():
    url = "https://www.akorda.kz/en/constitution-of-the-republic-of-kazakhstan-50912"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Извлекаем текст конституции (нужно будет настроить селекторы под конкретную структуру страницы)
        constitution_text = soup.get_text()
        
        # Создаем временный файл в памяти
        text_io = StringIO(constitution_text)
        loader = TextLoader(text_io)
        return loader.load()
    except Exception as e:
        print(f"Error loading constitution: {e}")
        return []
