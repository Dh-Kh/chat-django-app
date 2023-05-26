from django import forms
from .models import ChatNameHistory


class CreateChatForm(forms.ModelForm):
    class Meta:
        model = ChatNameHistory
        fields = ["chat_name"]

class SearchChatRoom(forms.Form):
    searching_of_chat = forms.CharField()