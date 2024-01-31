from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCreateUser(TestCase):

    def setUp(self):
        u1 = get_user_model('John', 'Mark', 'johnmark@gmail.com',
                            'test@pwd2023', 'test@pwd2023')
        u2 = get_user_model('Jane', 'Doe', 'janedoe@gmail.com',
                            'test@pwd2023', 'test@pwd2023')

    def tearDown(self):
        ...
        
    def test_fname_lname(self):
        self.assertContains()


if __name__ == '__main__':
    TestCase.main()
