import unittest
from app import create_app, db
from models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        """Set up a clean test environment before each test"""
        self.app = create_app('testing')  # Use test configuration
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

        db.create_all()  # Create tables for testing

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()
        self.ctx.pop()  # Remove app context

    def test_user_creation(self):
        """Test if a user can be created successfully"""
        user = User(name="John", email="john@example.com")
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.count(), 1)  # Check if user exists

if __name__ == '__main__':
    unittest.main()
