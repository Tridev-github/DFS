from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.username+self.password

class file_details(models.Model):
    owner = models.CharField(max_length=20)
    current_file = models.IntegerField()
    next_file = models.IntegerField()

class file_file(models.Model):
    file_owner = models.ForeignKey(file_details, on_delete=models.CASCADE)
    file_code = models.IntegerField()
    store_file = models.FileField(upload_to='DOWNLOADED_FILES',max_length=300)
