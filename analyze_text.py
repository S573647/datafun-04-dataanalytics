import requests

# Fetching the text
url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
response = requests.get(url)
text = response.text.lower()

print(text)