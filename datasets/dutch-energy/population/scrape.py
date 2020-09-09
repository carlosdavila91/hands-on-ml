import os
import pandas as pd
from bs4 import BeautifulSoup, NavigableString

DUTCH_PATH = os.path.join("datasets", "dutch-energy")
DATA_PATH = os.path.join(DUTCH_PATH, "population")
FILE_PATH = os.path.join(DATA_PATH, "dutch-population.html")

with open(FILE_PATH) as file:
    page = file.read()

soup = BeautifulSoup(page, 'html.parser')

#Parse data that are stored between <tr>..</tr> of HTML
rows = soup.find_all('tr')

print(rows[1])
# Columns
# col=[]
# i=0
# #For each row, store each first element (header) and an empty list
# for r in rows[0]:
#     name = r.string()
#     print('{}:"{}"'.format(i,name))
#     col.append((name,[]))
#     i += 1
