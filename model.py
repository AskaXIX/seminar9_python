from copy import deepcopy

PATH = 'phones.txt'
phone_book = {}
original_book = {}


def open_file():
    global phone_book, original_book, PATH
    with open(PATH, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        phone_book[1] = contact
    original_book = deepcopy(phone_book)


# def save_file():
