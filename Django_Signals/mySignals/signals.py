from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_succsess(sender, request, user, **kwargs):
    print("----------------")
    print("Login Signal ")
    print("Sender--",sender)
    print("Request--",request)
    print("user--",user)
    print(f"Kwargs--{kwargs}")

#user_logged_in.connect(login_succsess,sender=User) 

@receiver(user_logged_out, sender=User)
def logout_succsess(sender, request, user, **kwargs):
    print("----------------")
    print("LogOut Signal ")
    print("Sender--",sender)
    print("Request--",request)
    print("user--",user)
    print(f"Kwargs--{kwargs}")

#user_logged_out.connect(logout_succsess,sender=User) 

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("----------------")
    print("Login failed Signal ")
    print("Sender--",sender)
    print("Request--",request)
    print("credentials--",credentials)
    print(f"Kwargs--{kwargs}")

#user_login_failed.connect(login_failed) 