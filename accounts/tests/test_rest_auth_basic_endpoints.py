from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class TestRestAuthBasicEndpoints(APITestCase):
    """Test dj-rest-auth basic endpoints."""

    def setUp(self):
        """Set up test dependencies."""
        self.factory = RequestFactory()
        self.signup_url = reverse("rest_register")
        self.login_url = reverse("rest_login")
        self.logout_url = reverse("rest_logout")
        self.password_change_url = reverse("rest_password_change")
        self.password_reset_url = reverse("rest_password_reset")
        self.password_reset_confirm_url = reverse("rest_password_reset_confirm")
        self.user_data = {
            "email": "johndoe@gmail.com",
            "password1": "!!@)^!#)@Devil",
            "password2": "!!@)^!#)@Devil",
        }

    def test_signup(self):
        """Test signup endpoint."""
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["email"], self.user_data["email"])

    def test_login(self):
        """Test login endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data.get("email"),
                "password": self.user_data.get("password1"),
            },
        )  # login user
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["email"], self.user_data["email"])

    def test_logout(self):
        """Test logout endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data.get("email"),
                "password": self.user_data.get("password1"),
            },
        )  # login user
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["email"], self.user_data["email"])
        response = self.client.post(self.logout_url)  # logout user
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["detail"], "Successfully logged out.")

    def test_password_change(self):
        """Test password change endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data.get("email"),
                "password": self.user_data.get("password1"),
            },
        )
        access_token = response.data.get("access")

        headers = {"Authorization": f"Bearer {access_token}"}
        data = {
            "old_password": self.user_data.get("password1"),
            "new_password1": "!!@)^!#)@DevilNew",
            "new_password2": "!!@)^!#)@DevilNew",
        }
        response = self.client.post(self.password_change_url, data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["detail"], "New password has been saved.")

    def test_password_reset(self):
        """Test password reset endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.password_reset_url, {"email": self.user_data.get("email")}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["detail"], "Password reset e-mail has been sent."
        )

    def test_password_reset_confirm(self):
        """Test password reset confirm endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.password_reset_url, {"email": self.user_data.get("email")}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["detail"], "Password reset e-mail has been sent."
        )
        # retrieve email confirmation link

    def test_get_user_details(self):
        """Test user details endpoint."""
        response = self.client.post(
            self.signup_url, self.user_data
        )  # signup user first
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data.get("email"),
                "password": self.user_data.get("password1"),
            },
        )  # login user
        self.assertEqual(response.status_code, 200)
        access_token = response.data.get("access")
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.client.get(reverse("rest_user_details"), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.user_data.get("email"))

    def test_get_user_details_unauthorized(self):
        """Test user details endpoint."""
        response = self.client.get(reverse("rest_user_details"))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"], "Authentication credentials were not provided."
        )
