import json
from pathlib import Path


# Чтение файла json для выборки текстов
def load_text_form_file(file_name):
    file_path = Path(f"bot/messages/{file_name}")
    if (
        file_path.exists()
    ):  # возвращает true , если объект файловой системы существует, и false – если нет
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)  # Загружаем строку текста
    return "Файл не найден!"
