from django.db import models
from users.models import CustumUser
import random
# Create your models here.
class Code(models.Model):
    code = models.CharField(max_length=5,blank=True)
    user = models.OneToOneField(CustumUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

    def save(self, *args,**kwargs):
        num_list = [num for num in range(10)]
        code_item = ""
        for i in range(5):
            num = random.choice(num_list)
            code_item +=str(num)
        print('code--',code_item)
        self.code = code_item
        super().save(*args,**kwargs)