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
# get the table
table = soup.find('table')
# get all of the rows
rows = table.find_all('tr')
# itterate through all of the rows
for row in rows:
  tds = row.find_all('td')
  # check that it loaded the table and that it is a date row
  if tds and len(tds) > 1:
    # cehck that the style is not red, becuase red means that the host is down
    if "red" not in tds[0]['style']:
        try:
            # simple min algorithm after converting text in table to a float
            load = float(tds[len(tds) - 1].text.strip())
            if load < min_load:
                min_load = load
                min_machine = tds[0].text.strip()
                # return if the load is 0.0 since it can't get any better
                if load == 0.0:
                    break
        except ValueError:
            pass
            print("Invalid input: skipping maching and moving to the next")

print("Machine: %s" % min_machine)
print("Load: %f" % min_load)
