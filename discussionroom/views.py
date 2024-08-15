from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from users.tools import verify_login, random_key
from .models import Room
import random

KEY_LENGTH = 8

# Create your views here.

def home(request) :
    return render(request, "discussion_room.html")

class Register_room(View) :

    def get(self, request) :
        return render(request, "register_room.html")

    @verify_login
    def post(self, request) :
        sessid = request.POST['sessid']
        groupname = request.POST['name']
        about = request.POST['about']

        room = Room(name=groupname, key=random_key(KEY_LENGTH), about=about)
        room.save()

        return HttpResponse("Room booksed")

class Join_room(View) :

    def get(self, request) :
        return render(request, "join_room.html")

    @verify_login
    def post(self, request) :
        roomid = request.POST['roomid']
        roomkey = request.POST['roomkey']

        try :
            room = Room.objects.get(roomid=roomid)
            if (room.key == roomkey) :
                return HttpResponseRedirect(reverse("dcsroom:visit-room", kwargs={"roomid":roomid}))
            else :
                return HttpResponse("wroing rom key")
        except Room.DoesNotExist :
            return HttpResponse("Room Does not exists.")

def visit_room(request, roomid) :
    try:
        room = Room.objects.get(roomid=roomid)
        response = render(request, "visit_room.html", {
            "room": room
        })
        return response
    except Room.DoesNotExist :
        return HttpResponse("Room does not exisists")