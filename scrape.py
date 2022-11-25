import sys
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl

if len(sys.argv) < 3:
    print("Usage: python3 scrape.py <date> <xslx>")
    exit(1)

desired_date = sys.argv[1]
outpath = sys.argv[2]

url = 'https://discoveratlanta.com/events/all/'

result = rq.get(url)
## Your code here
src = result.content
soup = bs(src,'lxml')
scrape_dict={'title':[],'link':[]}

for article in soup.find_all('article',class_='listing'):
  date=str(desired_date)
  count=0
  if date in article['data-eventdates']:
    scrape_dict['link'].append(article.find('a')['href'])

    for div in article.findAll('div', attrs={'class':'listing-description'}):
      scrape_dict['title'].append(div.a.text)
scrape_df = pd.DataFrame(scrape_dict)
with pd.ExcelWriter(outpath) as writer:
    scrape_df.to_excel(writer,sheet_name='Event Details',index=False,na_rep='NaN')

wb = openpyxl.load_workbook(outpath)
sheet = wb.active
for column in sheet.columns:
  max_length_cell=0
  col_name= column[0].column_letter
  for cell in column:
    if len(str(cell.value))> max_length_cell:
      max_length_cell = len(str(cell.value))
  adj_width = max_length_cell
  sheet.column_dimensions[col_name].width = adj_width

wb.save(outpath)