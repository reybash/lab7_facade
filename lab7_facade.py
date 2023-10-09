import os

class FileFacade:
    def __init__(self):
        pass

    def create_file(self, filename):
        try:
            with open(filename, "w") as file:
                return f"Файл {filename} успешно создан."
        except Exception as e:
            return f"Ошибка при создании файла {filename}: {str(e)}"

    def delete_file(self, filename):
        try:
            os.remove(filename)
            return f"Файл {filename} успешно удален."
        except Exception as e:
            return f"Ошибка при удалении файла {filename}: {str(e)}"

    def list_files(self, directory):
        try:
            files = os.listdir(directory)
            return f"Список файлов в директории {directory}:\n{', '.join(files)}"
        except Exception as e:
            return f"Ошибка при получении списка файлов в директории {directory}: {str(e)}"

# Дополнительный фасад для записи в файл
class FileWriterFacade:
    def __init__(self):
        pass

    def write_to_file(self, filename, content):
        try:
            with open(filename, "a") as file:
                file.write(content + "\n")
            return f"Строка успешно добавлена в файл {filename}."
        except Exception as e:
            return f"Ошибка при записи в файл {filename}: {str(e)}"

# Дополнительный фасад для чтения из файла
class FileReaderFacade:
    def __init__(self):
        pass

    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                return f"Содержимое файла {filename}:\n{file.read()}"
        except Exception as e:
            return f"Ошибка при чтении файла {filename}: {str(e)}"
