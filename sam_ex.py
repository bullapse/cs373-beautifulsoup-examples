import requests
from bs4 import BeautifulSoup

def main():
        # Ask the user to search for a company's financial info
        sym = input("Please enter a company symbol:").upper()
        url = 'http://finance.yahoo.com/quote/' + sym + '?p=' + sym
        # Grab the HTML page from the url
        page = requests.get(url)

        # Parse the HTML page into a BeautifulSoup object
        soup = BeautifulSoup(page.text, 'html.parser')

        # Get the quote summary for the company on the page
        quote_summary = soup.find(id='quote-summary')

        if quote_summary is None:
            # If the company could not be found, the quote summary won't be there
            # Let the user know that
            print("Couldn't find any quote info for the company " + sym)
        else:
            # Go through all the table data in the quote summary and print the data
            for x in quote_summary.strings:
                print(x)


if __name__ == '__main__':
    main()
