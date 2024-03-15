from bs4 import BeautifulSoup
import requests

url = 'https://twitter.com/elonmusk'


# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://twitter.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html')

tweet_element = soup.find(attrs={'data-testid': 'tweetText'})

if tweet_element:
    print(tweet_element.text.strip())
else:
    print("Не удалось найти элемент с атрибутом data-testid='tweetText'")
