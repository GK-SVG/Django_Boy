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