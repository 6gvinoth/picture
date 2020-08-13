from djongo import models

class User(models.Model):
    user_name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length = 100)
    class Meta:
      db_table = "user"

    
