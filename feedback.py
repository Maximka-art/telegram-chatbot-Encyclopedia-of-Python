from open import open_file
import string


def check_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    for word in text.split():
        if word == "pep8" or word == "pep":  # pep8 - стандарт
            return open_file("pep8")
        elif word == "if" or word == "elif" or word == "else":  # if elif else - операторы условия
            return open_file("ifelifelse")
        elif word == "for" or word == "while":  # for и while - операторы цикла
            return open_file("forwhile")
        elif word == "print" or word == "input":  # print - напечатать и input - написать
            return open_file("printinput")
        elif word == "компилятор" or word == "интерпретатор":  # print - напечатать и input - написать
            return open_file("компилинтерп")
        elif word == "break":  # break - выход из цикла
            return open_file("break")
        elif word == "return":  # return - возвращение
            return open_file("return")
        else:
            return False
