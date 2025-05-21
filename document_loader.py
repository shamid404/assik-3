from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os

def load_documents(files):
    all_docs = []
    for file in files:
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            # Записываем содержимое загруженного файла во временный файл
            temp_file.write(file.getvalue())
            temp_file_path = temp_file.name
        
        try:
            # Используем путь к временному файлу для загрузки PDF
            loader = PyPDFLoader(temp_file_path)
            docs = loader.load()
            all_docs.extend(docs)
        finally:
            # Удаляем временный файл после использования
            os.unlink(temp_file_path)
            
    return all_docs
