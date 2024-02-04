from django.contrib.auth import get_user_model
from django.test import TestCase

"""
Tests for the User model and its functions.
"""

class UserManagersTests(TestCase):
    """
    Tests for the following functions:
        If user is created suncessfully.
        The values entered in fields email, password, is_active, is_stuff and is_supperuser
        when creating the user object.
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@mail.com", password="password")
        self.assertEqual(user.email, "test@mail.com")
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    """
    Tests for the following functions:
        If supperuser is created suncessfully.
        The values entered in fields email, password, is_active, is_stuff and is_supperuser
        when creating the superuser for admin functions
    """
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email="admin@mail.com", password="password"
        )
        self.assertEqual(user.email, "admin@mail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )
