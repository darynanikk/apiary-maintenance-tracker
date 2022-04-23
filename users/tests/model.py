from django.test import TestCase
from datetime import datetime
from ..models import User
from ..common import common



class TestAppModels(TestCase):

    def test_model_str(self):
        email = "darynadobro@gmail.com"
        is_verified = False
        first_name = "Test first name"
        last_name = "Test last name"
        phone = common.generate_random_phone()
        password = common.generate_random_phone()
        role = "simple"
        created_at = datetime.now()
        is_active = True
        user = User.objects.create_user(email=email, is_verified=is_verified, first_name=first_name,
                                   last_name=last_name, phone=phone, password=password,
                                   role=role, created_at=created_at, is_active=is_active)
        self.assertEqual(str(user), email)
