import unittest
from app import app
from models import db, User

class AppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_blogly_db'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up the database after each test."""
        with app.app_context():
            db.drop_all()

    def test_list_users_route(self):
        """Test the list users route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_user_route(self):
        """Test the add user route."""
        response = self.client.get('/create_user')
        self.assertEqual(response.status_code, 200)

    def test_post_user_route(self):
        """Test the post user route."""
        data = {'first_name': 'John', 'last_name': 'Doe', 'image_url': 'https://example.com/john_doe.jpg'}
        response = self.client.post('/create_user', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)

    def test_show_user_route(self):
        """Test the show user route."""
        # Assuming there is a user with ID 1 in the database
        user = User(first_name='John', last_name='Doe', image_url='https://example.com/john_doe.jpg')
        with app.app_context():
            db.session.add(user)
            db.session.commit()

        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)

if __name__ == '__main__':
    unittest.main()
