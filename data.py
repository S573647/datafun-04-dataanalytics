import requests
import csv
from io import StringIO

#logging.basicConfig(level=logging.INFO)

url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv' 
try:
    response = requests.get(url)
    if response.status_code == 200:
        #logging.info('Successfully fetched the movie data.')
        movie_data = response.content.decode('utf-8')

        # Use StringIO to treat the string as a file for csv.reader
        csv_reader = csv.reader(StringIO(movie_data))
        
        for row in csv_reader:
            # Each row is a tuple representing a movie
            movie_tuple = tuple(row)
            print(movie_tuple)
            # Now you can access data like movie_tuple[0] for title, movie_tuple[1] for year, etc.

    else:
        print("error")
        #logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    print("error")
    #logging.error(f'Failed to fetch data. Error: {e}')