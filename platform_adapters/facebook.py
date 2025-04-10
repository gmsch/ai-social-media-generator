from ai_model.generator import generate_post

def create_facebook_post(topic, title, description):
    return generate_post('Facebook', topic, title, description)
