import unittest
from ai_model.generator import generate_post

class TestAIGeneration(unittest.TestCase):
    def test_generation_not_empty(self):
        post = generate_post('Twitter', 'AI', 'AI surpasses humans', 'A new AI model surpassed human scores on a complex test.')
        self.assertTrue(bool(post))

if __name__ == '__main__':
    unittest.main()
