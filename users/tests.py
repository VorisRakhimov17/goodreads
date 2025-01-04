from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegisterTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                 'username': 'Voris',
                 'first_name': 'Voris',
                 'last_name':'Rakhimov',
                 'email':'VorisRakhimov17@gmail.com',
                 'password': 'somepassword'
             }
        )

        user = User.objects.get(username='Voris')

        self.assertEqual(user.first_name, 'Voris')
        self.assertEqual(user.last_name, 'Rakhimov')
        self.assertEqual(user.email, 'VorisRakhimov17@gmail.com')
        self.assertNotEqual(user.password, 'somepassword')
        self.assertTrue(user.check_password('somepassword'))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                'first_name': 'Voris',
                'email': 'VorisRakhimov17@gmail.com'
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                'username': 'Voris',
                'first_name': 'Voris',
                'last_name': 'Rakhimov',
                'email': 'invalid-email',
                'password': 'somepassword'
            }
        )
        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'email', 'This field is required.')

    def test_unique_username(self):
        # 1. Create a user
        user = User.objects.create(
            first_name='Voris',
            last_name='Rakhimov',
        )
        user.set_password('somepassword')
        user.save()

        # 2. try to create another user with that same username
        response = self.client.post(
            reverse("users:register"),
            data={
                'username': 'Voris',
                'first_name': 'Voris',
                'last_name': 'Rakhimov',
                'email': 'VorisRakhimov17@gmail.com',
                'password': 'somepassword'
            }
        )

        # 3. check that the second user was not created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains the error message
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')

class ProfileTestCase(TestCase):
    def test_login_required(self):
        self.client.post()
