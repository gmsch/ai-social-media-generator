from flask import Flask, render_template, request
from news_scraper.news_fetcher import fetch_news
from platform_adapters.twitter import create_twitter_post
from platform_adapters.facebook import create_facebook_post
from platform_adapters.linkedin import create_linkedin_post

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        news = fetch_news(topic)[0]

        twitter_post = create_twitter_post(topic, news['title'], news['description'])
        facebook_post = create_facebook_post(topic, news['title'], news['description'])
        linkedin_post = create_linkedin_post(topic, news['title'], news['description'])

        return render_template('index.html', topic=topic, news=news,
                               twitter_post=twitter_post, 
                               facebook_post=facebook_post,
                               linkedin_post=linkedin_post)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
