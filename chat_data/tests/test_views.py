from django.test import TestCase
from django.urls import reverse


class LoginMixin(TestCase):
    def setUp(self):
        self.response = self.client.login(username = "John Lennon", 
                                          password = "ImagineAllThePeoples")

class DashboardViewTest(LoginMixin):
    def test_case(self):
        self.response = self.client.get(reverse("chat_data:dashboard"))
        self.assertTrue(200, self.response.status_code)

class Chat_roomViewTest(LoginMixin):
    def test_case(self):
        self.response = self.client.get(reverse("chat_data:chat_room", args=["TheBeatles"]))
        self.assertTrue(200, self.response.status_code)


class Create_chat_roomViewTest(LoginMixin):
    def test_case(self):
        self.response = self.client.get(reverse("chat_data:create_chat_room"))
        self.assertTrue(200, self.response.status_code)


class Get_list_of_chat_roomsViewTest(LoginMixin):
    def test_case(self):
        url = reverse("chat_data:get_list_of_chat_rooms")
        self.response = self.client.get(url)
        self.assertTrue(200, self.response.status_code)


