import logging
import requests
import unicodedata



# Configure logging - change level to DEBUG and re-run, to ERROR and rerun 
logging.basicConfig(
  filename='text_analysis.log', 
  level=logging.INFO, 
  filemode='w', 
  format='%(name)s.%(levelname)s.%(message)s'
)

# Get a configured logger instance and name it logger
logger = logging.getLogger()


# Set url
url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
logger.debug(f"Requesting URL: {url}") 

# Request response object
response = requests.get(url)
logger.debug(f"Response object: {response}")

if response.status_code == 200:
    text = response.text.lower()
    logger.info("Fetched text successfully.")
else:
    logger.error(f"Failed to fetch text. Status code: {response.status_code}")
    text = ""

# Processing text data
words = text.split()
unique_words = set(words)
logger.info(f"Unique words count: {unique_words}")


# Writing unique words to a file
with open('unique_words.txt', 'w') as f:
    for word in unique_words:
        word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
        word = str(word).strip('b')
        f.write(str(word) + '\n')

logger.info("Unique words written to unique_words.txt")