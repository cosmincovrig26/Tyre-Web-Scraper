import requests
from bs4 import BeautifulSoup
import Tyre


def run():
    html = requests.get(
        f'https://www.national.co.uk/tyres-search?width={width}&profile={profile}&diameter={diameter}&pc=S601TG').text
    soup = BeautifulSoup(html, 'html.parser')
    tyreArray = soup.find_all('div', class_='tyreDisplay')
    for tyre in tyreArray:
        # brand
        brand = tyre['data-brand']
        # pattern
        myTyre = tyre.find('a', class_='pattern_link').text
        pattern = myTyre
        # size
        myTyre = tyre.find('div', class_='details')
        myTyre = myTyre.find_all('p')
        size = myTyre[1].text.replace(' ', '').replace('\r\n', '')
        size = size[0:6] + ' ' + size[6:9] + ' ' + size[9:12]
        # price
        myTyre = tyre['data-sort']
        price = myTyre
        # season
        season = tyre['data-tyre-season']
        # wet grip
        wetGrip = tyre['data-grip']
        # fuel efficiency
        fuelEfficiency = tyre['data-fuel']
        tyre = Tyre.Tyre(brand, pattern, size, price, season, wetGrip, fuelEfficiency)


print('Website: national.co.uk')
width = input('What is your tyre width? ')
profile = input('What is your tyre profile? ')
diameter = input('What is your tyre diameter? ')
run()  # scrape the website with the user input
Tyre.dbtosql()
print('Data successfully imported to database and exported as CSV')