from ntscraper import Nitter
from pprint import pprint

scraper = Nitter(log_level = 1, skip_instance_check = False)

tweets = scraper.get_tweets('elonmusk', mode = 'user', number = 10)

with open('tweets.txt', 'w') as file:
    # Записываем первые 10 строк в файл
    for i in range(10):
        try:
            tweet_text = tweets['tweets'][i]['text']
            file.write(tweet_text + '\n')  # Записываем текст твита и переходим на новую строку
        except IndexError:
            # Если индекс превышает количество доступных твитов, прекращаем запись
            break