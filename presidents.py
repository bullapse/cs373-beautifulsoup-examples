import requests
from bs4 import BeautifulSoup

# URL that we want to pull data from
url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States_by_previous_experience'

# default headers when making GET request
headers = requests.utils.default_headers()
headers.update(
	{
		'User-Agent': 'cs373-example'
	}
)

# Submits a GET request with the given URL
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


#print(soup) prints the entire HTML file
#print(soup.prettify()) prints entire HTML file with proper indentations


soup.title
#<title>List of Presidents of the United States by...</title>
soup.title.text
#'List of Presidents of the United States by previous experience'


# finds all table html tags
# table = soup.find_all('table')
table = soup.find('table')
trs = table.find_all('tr')

output = []
for row in trs[1:]: #skips the first row of headers
	output.append([cell.get_text(strip=True) for cell in row.find_all('td')])

#print out each name of presidents and their occupation
for item in output:
	print(item[2] + ": " + item[8])