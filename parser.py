from bs4 import BeautifulSoup
import requests


def parser_news():
    url = "https://batvinner.live/?gclid=CjwKCAjwl6OiBhA2EiwAuUwWZeORWsAkzJLbdRuEhUmHBwVnS_DhGuS-Xaf9V5f68V2OTo_PI6MZnxoC6-cQAvD_BwE"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.find_all("article", class_=lambda text: text and "elementor-post elementor-grid-item post" in text)
    info = [{"text": article.find("h3", class_="elementor-post__title").text.replace("\n", "").replace("\t", ""),
             "img": article.find("img")["src"], "link": article.find("a")["href"]} for article in articles]
    #result = [v for k, v in info[number].items()]
    #return " ".join(result)
    #convert = [data.values() for data in info]
    #result = [list(i) for i in convert]
    return info


parser_news()

