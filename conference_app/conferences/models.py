from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Conference(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField( max_length=100 )



    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)