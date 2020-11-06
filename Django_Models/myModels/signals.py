from django.db.models.signals import post_delete
from .models import Post
from django.dispatch import receiver

@receiver(post_delete,sender=Post)
def delete_user_with_post(sender,instance,**kwargs):
    print('User deleted with post')
    print('sender--',sender)
    instance.user.delete()