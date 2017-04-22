import requests
from bs4 import BeautifulSoup

def main():
    searching = True
    while(searching):
        sym = input("Please enter a company symbol:").upper()
        url = 'http://finance.yahoo.com/quote/' + sym + '?p=' + sym
        # Grab the HTML page from the url
        page = requests.get(url)

        # Parse the HTML page into a BeautifulSoup object
        soup = BeautifulSoup(page.text, 'html.parser')
        quote_summary = soup.find(id='quote-summary')

        if quote_summary is None:
            print("Couldn't find any quote info for the company " + sym)
        else:
            data = quote_summary.find('table')
            for x in data.strings:
                print(x)
        searching = input("Would you like to search for another company? (Y/N)").upper() == 'Y'

if __name__ == '__main__':
    main()
