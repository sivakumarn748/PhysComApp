from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import tools
from . import models
import uuid

# Create your views here.

class Register(View) :

    def get(self, request) :
        return HttpResponse("User Register page")

    def post(self, request) :
        return HttpResponse("User reg Post page")

class Login(View) :

    def get(self, request) :
        try:
            nexturl = request.GET['next']
        except:
            nexturl = ""
        return render(request, "userlogin.html", {
            'next': nexturl
        })

    def post(self, request) :
        username = request.POST['userid']
        password = request.POST['password']
        nexturl = request.POST['next']

        try: 
            user = models.User.objects.get(name=username)
            if (user.password == password) :
                sessid = uuid.uuid4()
                user.sessid = sessid
                user.save()
                return HttpResponse(f"""
                    <script>localStorage.setItem('sessid', '{str(sessid)}');alert(localStorage.getItem('sessid'));history.go(-2);</script>
                """)
            else :
                return HttpResponse("wrong password")
        except models.User.DoesNotExist :
            return HttpResponse("User Id Does not exists")

