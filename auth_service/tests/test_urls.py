from django.test import SimpleTestCase
from django.urls import reverse, resolve
from auth_service.views import (CreateUserAPIView, LoginAPIView,
                                VerifyEmail, ForgotPasswordView,
                                PasswordTokenCheckAPI, SetNewPasswordAPIView
                                )

class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('user_signup')
        self.assertEquals(resolve(url).func.view_class, CreateUserAPIView)

    def test_login_url_resolves(self):
        url = reverse('user_login')
        self.assertEquals(resolve(url).func.view_class, LoginAPIView)

    def test_verify_email_url_resolves(self):
        url = reverse('email-verify')
        self.assertEquals(resolve(url).func.view_class, VerifyEmail)

    def test_forgot_password_url_resolves(self):
        url = reverse('request-reset-email')
        self.assertEquals(resolve(url).func.view_class, ForgotPasswordView)

    def test_set_new_password_url_resolves(self):
        url = reverse('password-reset-complete')
        self.assertEquals(resolve(url).func.view_class, SetNewPasswordAPIView)

    # TODO with token