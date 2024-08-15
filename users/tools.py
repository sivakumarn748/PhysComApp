from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
import random
import string

def verify_login(function) :

    def inner (*args, **kwargs) :

        request = args[1]

        sessid = request.POST['sessid']

        if sessid == "" :
            return HttpResponseRedirect(reverse("users:login-user"))
        
        try :
            user = User.objects.get(sessid=sessid) 
        except User.DoesNotExist :
            return HttpResponseRedirect(reverse("users:login-user"))

        return function(*args, **kwargs)
    
    return inner

def random_key(length) :
    return "".join(random.choices(string.ascii_letters+string.digits, k=length))