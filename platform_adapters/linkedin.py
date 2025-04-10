from ai_model.generator import generate_post

def create_linkedin_post(topic, title, description):
    return generate_post('LinkedIn', topic, title, description)
