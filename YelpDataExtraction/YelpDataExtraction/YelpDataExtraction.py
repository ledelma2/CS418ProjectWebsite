
from bs4 import BeautifulSoup
import urllib.request
import csv


r = urllib.request.urlopen('https://www.yelp.com/biz/lowcountry-south-loop-chicago?frvs=True').read()
soup = BeautifulSoup(r, 'html.parser')


# table = soup.find('table')
# table = table.find_next('table')

# table_rows = table.find_all('tr')

with open('restaurant.csv', 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  csvwriter.writerow(['restaurantID', 'name', 'location', 'reviewCount', 'rating'])

  name = soup.find(class_='biz-page-title embossed-text-white')

  print(name.text.strip())

  

  # for row in table_rows:
    # cells = row.find_all('td')

    # if len(cells) > 0:

      # game (numeral)
      # game = cells[0].find('a').text

      # date (year)
      # year = cells[1].find('span')
      # year = year.find_next('span').text
      # year = year[len(year) - 4:]

      # winning team
      # winner = cells[2].find('span').text.rstrip(' !')

      #score
      # score = cells[3].find(class_='sorttext').text

      # loser
      # loser = cells[4].find('span').text.rstrip(' !')

      # venue
      # venue = cells[5].find('span').text.rstrip(' !')

      
      # write line to csv file
      # if (len(score) != 1):
       #  csvwriter.writerow([game, year, winner, score, loser, venue])
  

