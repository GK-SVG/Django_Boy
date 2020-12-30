from django.db import models
from django.contrib.auth.models import User
from .utills import generate_ref_code
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,blank=True)
    code = models.CharField(max_length=12,blank=True)
    recommend_by = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name="ref_by")
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}--{self.code}'
    
    def get_recommended_profile(self):
        pass

    def save(self, **args):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(**args)
     