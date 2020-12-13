import uuid 
from django.db import models 



class Custum_ID(models.Model): 
    custum_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    def __str__(self):
        return self.custum_id
    
    
class Custum_ID1(models.Model):
    custum_id1 = models.BigAutoField(primary_key=True,editable = False,default=1000)



    