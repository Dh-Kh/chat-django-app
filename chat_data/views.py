from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (CreateChatForm, SearchChatRoom)
from django.contrib import messages
from .models import ChatNameHistory, MessageHistory
from django.http import HttpResponse


@login_required
def dashboard(request):
    form = SearchChatRoom(request.POST)
    if request.method == "POST":
        if form.is_valid():
            mapping_data = form.cleaned_data["searching_of_chat"]
            for name_history in ChatNameHistory.objects.all().values("chat_name"):
                if name_history["chat_name"] == mapping_data:
                    return redirect(f"/chat_data/{mapping_data}/")
            if mapping_data not in ChatNameHistory.objects.all().values("chat_name"):
                messages.error(request, "This chat is not exist")
        else:
            messages.error(request, f"{form.errors}")
    context = {"form": form}    
    return render(request, "chat_data/dashboard.html", context)

@login_required
def chat_room(request, room_name):
    chat_data = MessageHistory.objects.filter(chat_name__chat_name=room_name).select_related("chat_name")
    restricted_access = ChatNameHistory.objects.filter(chat_name=room_name).exists()
    if restricted_access == False:
        return HttpResponse("No data available", 404)
    context = {"room_name": room_name, "chat_data": chat_data}
    return render(request, "chat_data/chat_room.html", context)

@login_required
def create_chat_room(request):
    form = CreateChatForm(request.POST)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            mapping_data = form.cleaned_data["chat_name"]
            for_save = form.save(commit=False)
            for_save.chat_creator = request.user.username
            for_save.save()
            return redirect(f"/chat_data/{mapping_data}/")
        else:
            messages.error(request, f"{form.errors}")
    
    return render(request, "chat_data/create_chat_room.html", context)

@login_required
def get_list_of_chat_rooms(request):
    context = {"list_of_chats": ChatNameHistory.objects.all()}
    return render(request, "chat_data/get_list_of_chat_rooms.html", context)