from django.db import models
from PIL import Image
import numpy as np
from .utills import get_filter_img
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
ACTION_CHOICES = (
    ('NO_FILTER','no_filter'),
    ('COLORIZED','colorized'),
    ('GRAYSCALE','grayscale'),
    ('BINARY','binary'),
    ('INVERT','invert'),
    ('BLURED','blured')
)



class Myupload(models.Model):
    img = models.ImageField(upload_to='images')
    action = models.CharField(max_length=100,choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        pil_img = Image.open(self.img)
        cv_img = np.array(pil_img)
        img = get_filter_img(cv_img,self.action)
        img = Image.fromarray(img)
        buffer = BytesIO()
        img.save(buffer,format='png')
        img_png = buffer.getvalue()
        self.img.save(str(self.img), ContentFile(img_png), save=False)
        return super().save(*args, **kwargs)