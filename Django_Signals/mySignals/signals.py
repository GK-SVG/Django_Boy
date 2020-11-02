from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete


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

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("----------------")
    print("Pre Save Signal at Beginning")
    print("Sender--",sender)
    print("Instance--",instance)
    print(f"Kwargs--{kwargs}")
    
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("----------------")
        print("Post Save Signal at Ending")
        print("New Record")
        print("Sender--",sender)
        print("Instance--",instance)
        print("created--",created)
        print(f"Kwargs--{kwargs}")
    else:
        print("----------------")
        print("Post Save Signal at Ending")
        print("Record Updated")
        print("Sender--",sender)
        print("Instance--",instance)
        print("created--",created)
        print(f"Kwargs--{kwargs}")

