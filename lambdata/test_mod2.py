"""To test example_module2"""
import unittest 
import example_module2 as oop
from random import randint


class SocialMediaUserTests(unittest.TestCase):
    """Test the Social Media User Class within example_module2.py"""

    def setUp(self):
        """Common setup code that runs before all test"""
        self.user1 = oop.SocialMediaClass(name="Jimmy", location="France")
        self.user2 = oop.SocialMediaClass(
            name="George Wazhington", location="Patagonia")
        self.user3 = oop.SocialMediaClass(
            name="Nick", location="New Zealand", upvotes=10605)
        
    def test_name_attribute(self):
            """Test the constructor method"""
            self.assertEqual(self.user1.name, "Jimmy")
            self.asserEqual(self.user2.name, "George Wazhinton")
            self.assertEqual(self.user3.name, "Nick")

    def test_location_attributes(self):
            """Test the constructor method"""
            self.assertEqual(self.user1.location, "France")

    def test_upvotes_attributes(self):
            """Test the constructor method"""
            self.assertEqual(self.user3.upvotes, 10605)
            self.assertEqual(self.user2.upvotes, 0)

    def test_unpopular(self):
        """Testing is_popular returns False when unpopular"""
        new_user = oop.SocialMediaClass("Johnny Bravo", "Wisconsin")
        self.asserFalse(new_user.is_popular())
        self.assertEqual(new_user.is_popular(), False)

    def test_popular(self):
        """Testing is_popular returns True when popular"""
        new_user.receive_upvotes(randint(101, 10000))
        self.new_user.receive_upvotes(randint(101, 10000))
        self.assertTrue(self.new_user.is_popular())





    if __name__ == "__main__":
        unittest.main()