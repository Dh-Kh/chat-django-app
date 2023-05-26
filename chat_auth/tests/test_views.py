from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from chat_auth.sensitive_ignore import First_ignore, Second_ignore
from chat_main import settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumMixin:
    def setUp(self):
        options = Options()
        options.binary_location = First_ignore
        self.selenium = webdriver.Firefox(executable_path=Second_ignore, options=options)
       
    def tearDown(self):
        self.selenium.quit()
        
class LoginTest(SeleniumMixin, LiveServerTestCase):
    def test_for_login_test(self):        
        self.selenium.get(self.live_server_url + "/chat_auth/login_user/")
        form_username = self.selenium.find_element(By.ID, 'id_username')
        form_username.send_keys('john')
        form_password = self.selenium.find_element(By.ID, 'id_password')
        form_password.send_keys('johnpassworD1234')
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()

class RegisterTest(SeleniumMixin, LiveServerTestCase):
    def test_for_register_test(self):
        self.selenium.get(self.live_server_url + "/chat_auth/register/")
        form_username = self.selenium.find_element(By.ID, 'id_username')
        form_username.send_keys('john')
        form_email = self.selenium.find_element(By.ID, 'id_email')
        form_email.send_keys("johnlennon@gmail.com")
        form_password1 = self.selenium.find_element(By.ID, 'id_password1')
        form_password1.send_keys('johnpassworD1234')
        form_password2 = self.selenium.find_element(By.ID, 'id_password2')
        form_password2.send_keys('johnpassworD1234')
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()
        
class ChangeUsernameTest(SeleniumMixin, LiveServerTestCase):
    def setUp(self):
        super().setUp()
        user = User.objects.create_user(username="John", password="YokoandJohn")
        self.client.force_login(user)  
        session_key = self.client.cookies[settings.SESSION_COOKIE_NAME].value
        self.selenium.get(self.live_server_url + "/chat_auth/login_user/")
        self.selenium.add_cookie({'name': settings.SESSION_COOKIE_NAME, 'value': session_key, 'path': '/'})
    def test_for_change_username(self):
        self.selenium.get(self.live_server_url + "/chat_auth/change_username/")
        form_username = self.selenium.find_element(By.ID, 'id_username')
        form_username.send_keys('john')
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()

class ChangeEmailTest(SeleniumMixin, LiveServerTestCase):
    def setUp(self):
        super().setUp()
        user = User.objects.create_user(username="John", password="YokoandJohn")
        self.client.force_login(user)  
        session_key = self.client.cookies[settings.SESSION_COOKIE_NAME].value
        self.selenium.get(self.live_server_url + "/chat_auth/login_user/")
        self.selenium.add_cookie({'name': settings.SESSION_COOKIE_NAME, 'value': session_key, 'path': '/'})
    def test_for_change_email(self):
        self.selenium.get(self.live_server_url + "/chat_auth/change_email/")
        form_email = self.selenium.find_element(By.ID, 'id_email')
        form_email.send_keys("johnlennon@gmail.com")
        form_verification = self.selenium.find_element(By.XPATH, '//input[@name="verification_field"]')
        form_verification.send_keys("123456")
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()
        
class ChangePasswordTest(SeleniumMixin, LiveServerTestCase):
    def setUp(self):
        super().setUp()
        user = User.objects.create_user(username="John", password="YokoandJohn")
        self.client.force_login(user)  
        session_key = self.client.cookies[settings.SESSION_COOKIE_NAME].value
        self.selenium.get(self.live_server_url + "/chat_auth/login_user/")
        self.selenium.add_cookie({'name': settings.SESSION_COOKIE_NAME, 'value': session_key, 'path': '/'})
        
    def test_for_change_password(self):
        self.selenium.get(self.live_server_url + "/chat_auth/change_password/")
        form_password0 = self.selenium.find_element(By.ID, 'id_old_password')
        form_password0.send_keys('johnpassworD1111')
        form_password1 = self.selenium.find_element(By.ID, 'id_new_password1')
        form_password1.send_keys('johnpassworD1234')
        form_password2 = self.selenium.find_element(By.ID, 'id_new_password2')
        form_password2.send_keys('johnpassworD1234')
        form_verification = self.selenium.find_element(By.XPATH, '//input[@name="verification_field"]')
        form_verification.send_keys("123456")
        submit_button = self.selenium.find_element(By.TAG_NAME, 'button')
        self.selenium.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button'))
            )
        submit_button.click()
        
        

        
        
    