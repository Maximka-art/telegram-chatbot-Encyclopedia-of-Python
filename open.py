def open_file(fileName):
    file = open(f".//answers//{fileName}.txt", "r", encoding='utf-8')
    words = file.read()
    file.close()
    return words
