from bs4 import BeautifulSoup

from requests import get

url = "http://apps.cs.utexas.edu/unixlabstatus/"

# get the html page
r = get(url)
data = r.text

# Create the Python Object from HTML
soup = BeautifulSoup(data, "html.parser")

# globals
min_load = 1000.0
min_machine = ''
# get every table row in the table
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
  tds = row.find_all('td')
  # check that it loaded the table and that the the row is not red
  if tds and len(tds) > 1:
    if "red" not in tds[0]['style']:
        try:
            load = float(tds[len(tds) - 1].text.strip())
            if load < min_load:
                min_load = load
                min_machine = tds[0].text.strip()
        except ValueError:
            pass
            print("Invalid input: skipping maching and moving to the next")

print("Machine: %s" % min_machine)
print("Load: %f" % min_load)
