from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    rel_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Crew(models.Model):
    actor = models.CharField(max_length=50)
    acteress = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie,related_name='movie',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie} {self.actor} {self.acteress}'
    
