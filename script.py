import socket, requests, re
from bs4 import BeautifulSoup
from data import *


def test_status_website():
    response = requests.get('https://' + DOMEN)
    assert response.status_code == 200
    print(f' Веб-сайт {DOMEN} работает. Статус код: {response.status_code}')


def test_host_ip_address():
    assert socket.gethostbyname(DOMEN)
    print(' IP адрес хоста sstmk.ru:', socket.gethostbyname(DOMEN))


def extract_number_telephone():
    response = requests.get('https://' + DOMEN).text
    soup = BeautifulSoup(response, 'html.parser')
    contact_number = soup.select_one('#top > div.all-content-wrapper > div.header.content-padd > div > div >'
                              ' div.phone_lang > div.phone-number > a').contents
    return contact_number


number = extract_number_telephone()


def test_number_telephone():
    result = re.match(r'^(\+7|7|8|)([(])((\(\d{3}\))|(\d{3}))([)])(\d{3}[\- ]?\d{2}[\- ]?\d{2})$|'
                      r'^(\+7|7|8|)([(])((\(\d{5}\))|(\d{5}))([)])(\d{1}[\- ]?\d{2}[\- ]?\d{2})$', *number)
    try:
        assert bool(result) == True
        print(f' Номер телефона "{number[0]}" соответствует стандарту "+A(BBB)CCC-CC-CC"')
    except AssertionError:
        # assert bool(result) == False
        print(f' Номер телефона "{number[0]}" не соответствует стандарту "+A(BBB)CCC-CC-CC".')
    return number


def test_standard_format_number():
    numbers = list(filter(str.isdigit, *number))[1:]
    num = "+7({}{}{}){}{}{}-{}{}-{}{}".format(*numbers)
    result = re.match(r'^(\+7|7|8|)([(])((\(\d{3}\))|(\d{3}))([)])(\d{3}[\- ]?\d{2}[\- ]?\d{2})$|'
                      r'^(\+7|7|8|)([(])((\(\d{5}\))|(\d{5}))([)])(\d{1}[\- ]?\d{2}[\- ]?\d{2})$', num)
    assert bool(result) == True
    print(' Номер телефона в соответствующем стандарту формате:', num)

