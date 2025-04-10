from newsapi import NewsApiClient
import yaml

with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

newsapi = NewsApiClient(api_key=config["newsapi_key"])

def fetch_news(topic, num_articles=1):
    top_headlines = newsapi.get_everything(q=topic, language='en', sort_by='relevancy', page_size=num_articles)
    articles = top_headlines['articles']
    return [{"title": article["title"], "description": article["description"]} for article in articles]
