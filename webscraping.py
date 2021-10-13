from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/top'
response = get(url)

html_soup = BeautifulSoup(response.text,'html.parser')

titleLines = html_soup.find_all('td',{'class':'titleColumn'})
ratingLines = html_soup.find_all('td',{'class':'ratingColumn imdbRating'})

title, position, rating = [], [], []

for i in range(100):
    children = titleLines[i].findChildren("a")
    movieRating = ratingLines[i].findChildren("strong")
    title.append(children[0].get_text())
    position.append(i+1)
    rating.append(movieRating[0].get_text())
    
df = pd.DataFrame({'Position' : position, 'Title': title, 'Rating': rating})
df.head(10)