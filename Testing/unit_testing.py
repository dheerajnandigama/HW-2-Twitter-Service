""""
Unit Testing:
Testing functions were added to ensure the functionality of functions and APIs worked as expected for a better user experience.

Developer: Asish Raju Vachavaya 

"""
import unittest
from flask import Flask
from app import app

class esp_twitter_unitZ_tes(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()

    def test_twitter_create_post(self):
        print("Testing create post function!")
        res_1 = self.app.post('https://www.google.com/url?q=http://127.0.0.1:5000/api/posts&source=gmail-imap&ust=1695607298000000&usg=AOvVaw2aUyUzX3Ry5ZT9DIz392e8', json={'text': 'Test post'})
        self.assertEqual(res_1.status_code, 204)

    def test_twitter_delete_post(self):
        print("Testing delete post function!")
        self.app.post('/https://www.google.com/url?q=http://127.0.0.1:5000/api/posts&source=gmail-imap&ust=1695607298000000&usg=AOvVaw2aUyUzX3Ry5ZT9DIz392e8', json={'text': 'Test post', 'id': 1})
        res_2 = self.app.delete('/api/posts/1')
        self.assertEqual(res_2.status_code, 204)

if __name__ == '__main__':
    print("Iniating tesing for ESP HW2")
    unittest.main()