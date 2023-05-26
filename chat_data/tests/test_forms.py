from django.test import TestCase
from chat_data.forms import (CreateChatForm, SearchChatRoom)

class CreateChatFormTest(TestCase):
    def test_for_create_chat_form(self):
        form = CreateChatForm(data = {
            "chat_name": "History",
            "chat_creator": "Teacher"
        })
        self.assertTrue(form.is_valid())
        
class SearchChatRoomTest(TestCase):
    def test_for_search_chat_room(self):
        form = SearchChatRoom(data = {
            "searching_of_chat": "History"
        })
        self.assertTrue(form.is_valid())