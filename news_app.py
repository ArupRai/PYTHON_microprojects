import requests
import time
url = ('https://newsapi.org/v2/everything?q=bitcoin&apiKey=b833ffd0c3914e88bfe780f8bc2dfef5')


response = (requests.get(url)).text

for news in response.split(","):
    print(news)
    time.sleep(2)
