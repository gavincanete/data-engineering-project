import requests
from bs4 import BeautifulSoup as bs

import re

def shoe_extraction_with_two_columns(type='men'):
    # Request tayew.com
    url = 'http://www.tayew.com/'+type+'.html'
    req = requests.get(url)

    # Create HTML tree
    soup = bs(req.content, 'html.parser')

    # Locate the shoe table component
    s = soup.find('div', id='t_frame')
    table = s.find('table')

    tables = table.find_all('td')


    """ 
    - Filter the text with 'stock' label
    - Reformat the filtered text into one line
    """
    stocks = []

    for row in tables:
        temp_text = row.text.strip()
        if('stock' in temp_text):
            stocks.append(temp_text.replace('\r\n', ''))


    # Break each statement into 4 fields (stock#, color, sizes and description)
    formatted_stocks = []
    for stock in stocks:
        temp = stock.split()
        temp[0] = temp[0].replace('stock#','')
        temp[0] = re.sub('-[a-z]*[A-Z]*', '', temp[0])              

        formatted_stock = {
            'stock_number': temp[0], 
            'color': temp[1], 
            'sizes': ' '.join(temp[4:8]) if '1/2' in temp else ' '.join(temp[4:7]),
            'description': ' '.join(temp[8:]) if '1/2' in temp else ' '.join(temp[7:])
        }
        formatted_stocks.append(formatted_stock)

    # Indicate field header
    shoes_info = ['stock_number','color','sizes','description']

    return shoes_info, formatted_stocks

def shoe_extraction_with_three_columns(type='uniform'):
    # Need to implement
    return None