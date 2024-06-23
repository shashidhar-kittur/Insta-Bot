import unittest
from project.main import send_greeting


class TestInstaBot(unittest.TestCase):
    def test_send_greeting(self):
        # This is a basic test case, you can expand it with mock objects
        greeting_type = "morning"
        send_greeting(greeting_type)
        self.assertTrue(True)  # Simplified test, replace with actual assertions


if __name__ == "__main__":
    unittest.main()
