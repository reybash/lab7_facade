import lab7_facade as facade

# Использование фасадов
def main():
    file_facade = facade.FileFacade()
    file_writer_facade = facade.FileWriterFacade()
    file_reader_facade = facade.FileReaderFacade()

    result1 = file_facade.create_file("example.txt")
    print(result1)

    result2 = file_facade.list_files(".")
    print(result2)

    result3 = file_writer_facade.write_to_file("example.txt", "Это строка, которую добавил пользователь")
    print(result3)

    result4 = file_facade.list_files(".")
    print(result4)

    result4 = file_reader_facade.read_file("example.txt")
    print(result4)

    result5 = file_facade.delete_file("example.txt")
    print(result5)

if __name__ == "__main__":
    main()