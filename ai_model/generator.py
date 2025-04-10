import openai
import yaml

with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

openai.api_key = config["openai_api_key"]

def generate_post(platform, topic, news_title, news_description):
    prompt = f"For {platform}, create a provocative and engaging social media post based on the following news headline and summary.\n\nHeadline: '{news_title}'\nSummary: '{news_description}'\n\nPost:"
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a social media specialist."},
          {"role": "user", "content": prompt}
      ],
      max_tokens=100
    )

    return response.choices[0].message.content.strip()
