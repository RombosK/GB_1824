import requests
import xml.etree.ElementTree as ET


def currency_rates(char_code):
    char_code = char_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)

    for valute in ET.fromstring(response.text).findall('Valute'):
        if char_code == valute.find('CharCode').text:
            return float(valute.find('Value').text.replace(',', '.'))

    return


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))