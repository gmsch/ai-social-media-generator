from ai_model.generator import generate_post

def create_twitter_post(topic, title, description):
    generated = generate_post('Twitter', topic, title, description)
    if len(generated) > 280:
        return generated[:277] + "..."
    return generated
