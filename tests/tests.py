import unittest
from src.ans import is_username_available


class TestIsUsernameAvailable(unittest.TestCase):
    def test_username_availability(self):
        current_users = ['admin', 'user1', 'testuser']
        new_users = ['User1', 'guest', 'Admin']
        expected = [False, True, False]  # 'User1' and 'Admin' are taken
        self.assertEqual(is_username_available(
            current_users, new_users), expected)

    def test_all_available(self):
        current_users = ['user1', 'user2']
        new_users = ['user3', 'user4']
        self.assertEqual(is_username_available(
            current_users, new_users), [True, True])

    def test_empty_new_users(self):
        self.assertEqual(is_username_available(['admin', 'user1'], []), [])


if __name__ == '__main__':
    unittest.main()
